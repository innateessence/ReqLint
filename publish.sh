#!/usr/bin/env bash

pip install twine build
python -m build --sdist --wheel
twine upload dist/*
rm -rf build dist ReqLint.egg-info
