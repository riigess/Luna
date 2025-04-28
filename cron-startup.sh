#!/bin/bash

proj_dir="/root/code"

runner() {
    cd $proj_dir/Luna
    if [ -f .luna-venv/bin/activate ]; then
        echo ".luna-venv exists (check passed)"
        source .luna-venv/bin/activate
    else
        echo ".luna-venv does not exist (check not passed)"
        python3 -m venv .luna-venv
        source .luna-venv/bin/activate
        pip3 install -r requirements.txt
    fi
    echo "Updating directory with git"
    git pull
    cd src
    echo "Starting bot"
    python3 main.py
    runner
}

# If there is nothing running in /root/luna/src
if [[ -z "$(ps -auxe | grep "python3" | grep "PWD=$proj_dir/Luna/src" | grep -v grep)" ]]; then
    runner
else
    echo "Already running"
fi
