#!/bin/bash -e
flake8 ./app
black --check ./app
find ./app -type f -name "*.py" -exec isort -c {} \;
