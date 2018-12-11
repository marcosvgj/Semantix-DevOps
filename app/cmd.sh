#!/bin/bash
set -e

if [ "$ENV" = 'UNIT' ]; then
  echo "Test Unit"
  exec python3 "TestCase.py"
else
  echo "Dev API"
  exec python3 "app.py"
fi



