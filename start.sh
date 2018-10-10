#!/bin/sh

until sudo python app/main.py; do
    echo "Flask crashed with exit code $?. Restarting..." >&2
    sudo pkill -9 python
    sleep 1
done
