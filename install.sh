#!/bin/bash

set -e
conda env create -n masking -f environment.yaml
conda run -n masking python3 -m pip install .
