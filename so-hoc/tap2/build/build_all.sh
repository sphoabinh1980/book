#!/bin/bash
# Dựng lại toàn bộ "Số học — Tập 2": biên dịch lời giải mẫu, kiểm tra, vẽ hình, dựng .docx hai lượt và xuất .pdf
set -e
cd "$(dirname "$0")/.."
python3 build/compile.py
python3 verify/run.py
(cd figs && for f in front.py ch*.py; do python3 "$f"; done)
python3 build/paginate.py ..
