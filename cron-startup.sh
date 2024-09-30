#!/bin/bash

proj_dir="/home/riigess/Github"

runner() {
    cd $proj_dir/Mona
    if [ -f .mona-venv/bin/activate ]; then
        echo ".mona-venv exists (check passed)"
        source .mona-venv/bin/activate
    else
        echo ".mona-venv does not exist (check not passed)"
        python3 -m venv .mona-venv
        source .mona-venv/bin/activate
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
if [[ -z "$(ps -auxe | grep "python3" | grep "PWD=$proj_dir/Mona/src" | grep -v grep)" ]]; then
    runner
else
    echo "Already running"
fi
