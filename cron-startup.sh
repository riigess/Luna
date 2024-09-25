#!/bin/bash

runner() {
    cd /home/riigess/Documents/Github/Mona
    if [ -f .venv/bin/activate ]; then
        echo ".venv exists (check passed)"
        source .venv/bin/activate
    else
        echo ".venv does not exist (check not passed)"
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
