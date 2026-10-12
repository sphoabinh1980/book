#!/bin/bash
# Dựng lại toàn bộ "Số học — Tập 1": vẽ hình, biên dịch và sinh output ví dụ, kiểm tra code, dựng .docx hai lượt và xuất .pdf
set -e
cd "$(dirname "$0")/.."
(cd figs && for f in front.py ch*.py; do python3 "$f"; done)
python3 build/run_examples.py
python3 build/check_code.py
python3 build/paginate.py ..
