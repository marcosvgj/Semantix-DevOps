#!/usr/bin/env bash

set -e

if [ "$ENV" = 'UNIT' ]; then
  echo "Running Test Cases"
  exec python3 "TestCase.py"
else
  echo "Running Production Server"
  exec python3 "app.py"
fi