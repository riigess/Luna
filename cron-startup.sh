#!/bin/bash

runner() {
    cd /root/mona
    git pull
    cd src
    python3 main.py
    runner
}

runner
