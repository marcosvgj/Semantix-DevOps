#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "** Running Server **"
    exec python3 "app.py"
elif [ "$ENV" = 'UNIT' ];then
    echo " ** Running Unit Test ** "
	exec python3 "TestCase.py"
else
    echo "** Option doesn't recognized ** "
fi


