#!/usr/bin/env python3
"""
clo_rollup.py — Roll Canvas criterion-level outcomes up into final CLO scores.

Context (Option B):
  Each rubric criterion is keyed into Canvas Outcomes as its own outcome,
  named like "CLO1.1 Correctness", "CLO1.2 Use of constructs", etc.
  Canvas can aggregate each outcome ACROSS activities over time (its
  calculation method: decaying average / most recent / ...), but it CANNOT
  average the criterion-outcomes of one CLO into a single CLO score.

  This script does exactly that missing step:
    final CLO_n (per student) = mean( criterion-outcome scores whose title
                                      starts with "CLO_n." )
  using the already-aggregated scores Canvas returns from /outcome_rollups.

Outputs two CSVs:
  clo_final.csv      — one row per student, one column per CLO (the averages)
  criterion_detail.csv — one row per student, every criterion score (audit trail)

Requires only the Python standard library (no pip install).

Setup:
  set CANVAS_BASE_URL=https://<your-institution>.instructure.com   (no trailing slash)
  set CANVAS_TOKEN=<your personal access token>
  set CANVAS_COURSE_ID=<numeric course id>
Then:
  python clo_rollup.py
"""

import csv
import json
import os
import re
import sys
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Configuration (env vars override these defaults)
# ---------------------------------------------------------------------------
BASE_URL  = os.environ.get("CANVAS_BASE_URL", "").rstrip("/")
TOKEN     = os.environ.get("CANVAS_TOKEN", "")
COURSE_ID = os.environ.get("CANVAS_COURSE_ID", "")

# How to extract the CLO key from an outcome title.
#   "CLO1.1 Correctness" -> group(1) == "CLO1"
# Adjust if you name outcomes differently.
CLO_PATTERN = re.compile(r"^\s*(CLO\d+)", re.IGNORECASE)

# If a student has no score for a criterion (null), should it count as 0
# ("No Evidence") in the CLO average, or be excluded from the average?
#   False -> average only the criteria actually assessed so far (fairer mid-term)
#   True  -> treat missing as 0 (strict; matches a "0 = No Evidence" reading)
MISSING_AS_ZERO = False

# Mark mastery in the final CSV when CLO average >= this (your Level 3).
MASTERY_THRESHOLD = 3.0
# ---------------------------------------------------------------------------


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def api_get(path, params=None):
    """GET a Canvas API path, following Link-header pagination.

    Returns the concatenation of the top-level JSON across pages. The
    /outcome_rollups payload is an object (rollups + linked); we merge those
    pieces across pages.
    """
    if params is None:
        params = {}
    url = f"{BASE_URL}/api/v1/{path.lstrip('/')}"
    query = urllib.parse.urlencode(params, doseq=True)
    if query:
        url = f"{url}?{query}"

    merged_rollups = []
    merged_linked = {}
    plain_pages = []  # for endpoints that return a bare list

    while url:
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
        try:
            with urllib.request.urlopen(req) as resp:
                body = resp.read().decode("utf-8")
                link_header = resp.headers.get("Link", "")
        except urllib.error.HTTPError as e:
            die(f"HTTP {e.code} on {url}\n{e.read().decode('utf-8', 'replace')}")
        except urllib.error.URLError as e:
            die(f"Network error on {url}: {e.reason}")

        data = json.loads(body)
        if isinstance(data, list):
            plain_pages.extend(data)
        else:
            merged_rollups.extend(data.get("rollups", []))
            for key, val in data.get("linked", {}).items():
                merged_linked.setdefault(key, []).extend(val)

        # Find rel="next" in the Link header
        url = None
        for part in link_header.split(","):
            seg = part.split(";")
            if len(seg) >= 2 and 'rel="next"' in seg[1]:
                url = seg[0].strip().lstrip("<").rstrip(">")
                break

    if plain_pages:
        return plain_pages
    return {"rollups": merged_rollups, "linked": merged_linked}


def main():
    if not (BASE_URL and TOKEN and COURSE_ID):
        die("Set CANVAS_BASE_URL, CANVAS_TOKEN and CANVAS_COURSE_ID first.")

    print(f"Fetching outcome rollups for course {COURSE_ID} ...")
    data = api_get(
        f"courses/{COURSE_ID}/outcome_rollups",
        {
            "include[]": ["outcomes", "users"],
            "per_page": 100,
            # Skip rows with no data at all so the CSV stays clean:
            "exclude[]": ["missing_user_rollups"],
        },
    )

    rollups = data["rollups"]
    linked = data["linked"]

    # outcome_id -> title  (from linked.outcomes; fall back to /outcomes/:id)
    title_by_id = {}
    for o in linked.get("outcomes", []):
        title_by_id[str(o["id"])] = o.get("title", f"outcome {o['id']}")

    def outcome_title(oid):
        oid = str(oid)
        if oid not in title_by_id:
            o = api_get(f"outcomes/{oid}")
            title_by_id[oid] = o.get("title", f"outcome {oid}") if isinstance(o, dict) else f"outcome {oid}"
        return title_by_id[oid]

    # outcome_id -> CLO key (e.g. "CLO1"), via the title naming convention
    clo_by_outcome = {}
    all_criteria_titles = {}  # title -> CLO key, for the detail CSV header
    for oid in list(title_by_id.keys()):
        title = title_by_id[oid]
        m = CLO_PATTERN.match(title)
        if m:
            clo_by_outcome[oid] = m.group(1).upper()
            all_criteria_titles[title] = m.group(1).upper()

    if not clo_by_outcome:
        die("No outcomes matched the CLO naming pattern. Check CLO_PATTERN or "
            "your outcome titles (expected e.g. 'CLO1.1 Correctness').")

    clo_keys = sorted(set(clo_by_outcome.values()),
                      key=lambda k: int(re.sub(r"\D", "", k) or 0))
    criterion_cols = sorted(all_criteria_titles.keys())

    final_rows = []
    detail_rows = []

    for r in rollups:
        student = r.get("name", "")
        user_id = r.get("links", {}).get("user", "")

        # Gather this student's criterion scores grouped by CLO
        per_clo = {k: [] for k in clo_keys}
        detail = {"student": student, "user_id": user_id}

        for s in r.get("scores", []):
            oid = str(s.get("links", {}).get("outcome", ""))
            clo = clo_by_outcome.get(oid)
            if clo is None:
                continue
            title = outcome_title(oid)
            score = s.get("score")
            detail[title] = "" if score is None else score
            if score is None:
                if MISSING_AS_ZERO:
                    per_clo[clo].append(0.0)
                # else: skip
            else:
                per_clo[clo].append(float(score))

        final = {"student": student, "user_id": user_id}
        for clo in clo_keys:
            vals = per_clo[clo]
            if vals:
                avg = round(sum(vals) / len(vals), 2)
                final[clo] = avg
                final[f"{clo}_mastery"] = "Y" if avg >= MASTERY_THRESHOLD else "N"
                final[f"{clo}_n"] = len(vals)
            else:
                final[clo] = ""
                final[f"{clo}_mastery"] = ""
                final[f"{clo}_n"] = 0

        final_rows.append(final)
        detail_rows.append(detail)

    # ---- write clo_final.csv ----
    final_cols = ["student", "user_id"]
    for clo in clo_keys:
        final_cols += [clo, f"{clo}_mastery", f"{clo}_n"]
    with open("clo_final.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=final_cols)
        w.writeheader()
        w.writerows(final_rows)

    # ---- write criterion_detail.csv ----
    detail_cols = ["student", "user_id"] + criterion_cols
    with open("criterion_detail.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=detail_cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(detail_rows)

    print(f"Done. {len(final_rows)} students, CLOs: {', '.join(clo_keys)}")
    print("Wrote clo_final.csv and criterion_detail.csv")


if __name__ == "__main__":
    main()
