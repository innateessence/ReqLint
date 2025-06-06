#!/usr/bin/env bash

pip install twine build
python -m build --sdist --wheel
twine upload dist/*
rm -rf build dist py_reqlint.egg-info
