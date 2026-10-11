#!/bin/bash
# Dựng lại toàn bộ Tập 3 từ mã nguồn:
#   1) chấm mọi chương trình trong code/ trên bộ test sinh từ tgen/ (ghi judge/scores.json),
#   2) vẽ sơ đồ khối, 3) dựng .docx hai lượt (đánh số trang mục lục) và xuất .pdf
# Cần các lời giải mẫu của Tập 2 đã được biên dịch (../tap2/sol) để sinh đáp án cho test.
set -e
cd "$(dirname "$0")/.."
for f in ../tap2/sol/*.cpp; do [ -x "${f%.cpp}" ] || g++ -O2 -std=c++17 -o "${f%.cpp}" "$f"; done
[ "$1" = "--no-judge" ] || python3 -u judge/judge.py
(cd figs && for f in flows_ch*.py; do python3 "$f"; done)
python3 build/paginate.py ..
