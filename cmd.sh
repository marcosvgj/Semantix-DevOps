#!/bin/bash
set -e

if [ "$ENV" = 'UNIT' ]; then
  echo "Test Unit"
  exec python "TestCase.py"
else
  echo "Dev API"
  exec python "app.py"
fi



