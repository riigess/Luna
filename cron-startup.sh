#!/bin/bash

runner() {
    cd /root/mona
    git pull
    cd src
    python3 main.py
    runner
}

# If there is nothing running in /root/mona/src
if [[ -z "$(ps -auxe | grep "python3" | grep "PWD=/root/mona/src" | grep -v grep)" ]]; then
    runner
else
    echo "Already running"
fi
