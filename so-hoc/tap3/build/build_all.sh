#!/bin/bash
# Dựng lại toàn bộ "Số học — Tập 3": chấm mọi cách làm, vẽ sơ đồ khối, dựng .docx hai lượt và xuất .pdf
# (cần Tập 2 đã dựng xong để có số trang đề bài: ../tap2/build/pages.json)
set -e
cd "$(dirname "$0")/.."
[ "$1" = "--no-judge" ] || python3 -u judge/judge.py
python3 build/check_code.py
(cd figs && for f in front.py flows_ch*.py; do python3 "$f"; done)
python3 build/paginate.py ..
