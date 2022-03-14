#!/bin/sh

if [ ! -d "venv" ]; then
  python -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
fi

source venv/bin/activate
mpiexec -n $1 python counter.py --mca opal_warn_on_missing_libcuda 0 --slots=$1
