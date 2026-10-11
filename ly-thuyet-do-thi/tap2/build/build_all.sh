#!/bin/bash
# Dựng lại toàn bộ Tập 2 từ mã nguồn:
#   1) biên dịch lời giải mẫu, 2) vẽ hình, 3) dựng .docx hai lượt (đánh số trang mục lục), 4) xuất .pdf
set -e
cd "$(dirname "$0")/.."
for f in sol/*.cpp; do g++ -O2 -std=c++17 -o "${f%.cpp}" "$f" 2>/dev/null; done
(cd figs && for f in ch1 ch2 ch3 ch4 ch5 front; do python3 $f.py; done)
python3 build/paginate.py ..
