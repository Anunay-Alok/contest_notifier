#!/bin/bash
python3 notifier.py > log.txt
notify-send -t 10000 "$(basename log.txt)" "$(cat log.txt)"
rm log.txt
rm file0.txt