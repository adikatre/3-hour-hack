#!/bin/bash

# USAGE: run `source scripts/venv.sh` in the root directory of this repository.

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt