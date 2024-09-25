#!/bin/bash

runner() {
    cd /root/mona
    if [ -f .venv/bin/activate ]; then
        echo ".venv exists (check passed)"
    else
        python3 -m venv .venv
        source .venv/bin/activate
        pip3 install -r requirements.txt
    fi
    echo "Updating directory with git"
    git pull
    cd src
    echo "Starting bot"
    python3 main.py
    runner
}

# If there is nothing running in /root/mona/src
if [[ -z "$(ps -auxe | grep "python3" | grep "PWD=/home/riigess/Documents/Mona/src" | grep -v grep)" ]]; then
    runner
else
    echo "Already running"
fi
