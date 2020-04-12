#!/bin/bash
set -veuxo pipefail

python3.8 -m mypy
python3.8 -m black src
flake8 --count --select=E9,F63,F7,F82 --show-source --statistics src
flake8 --count --max-line-length=88 --statistics src
