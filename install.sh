#!/bin/bash

set -e
env=masking
conda create -f environments.yaml -n $(env)
conda run -n $(env) python3 -m pip install .
