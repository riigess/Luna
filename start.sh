#!/bin/sh
output="$(ps -aux | grep python3 | grep -v grep)"

if [[ -n $output ]]; then
   echo Already running..
else
   cd /home/pi/arata-discord
   git pull
   cd src
   python3 main.py
fi