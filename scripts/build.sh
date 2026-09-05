#!/usr/bin/env bash
# Build the claude.ai upload zip from the skill folder. The repo is the source of truth; dist/ is derived.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import re,sys
t=open('ti-fantasy-coach/SKILL.md').read()
m=re.search(r'^description:\s*(.*)$',t,re.M)
assert m, 'SKILL.md missing description'
n=len(m.group(1)); assert n<=200, f'description is {n} chars (claude.ai cap 200)'
print(f'description ok ({n} chars)')
PY
python3 ti-fantasy-coach/scripts/ev_calc.py ti-fantasy-coach/templates/banner_state.json --samples 500 >/dev/null && echo "ev_calc ok"
rm -rf dist && mkdir dist
zip -qr dist/ti-fantasy-coach.zip ti-fantasy-coach -x "*.DS_Store" -x "*/__pycache__/*"
echo "built dist/ti-fantasy-coach.zip -> upload at claude.ai Settings > Skills (replaces previous version)"
