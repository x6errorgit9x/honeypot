#!/bin/sh
python init_db.py

python honeypot.py &

python dashboard.py
