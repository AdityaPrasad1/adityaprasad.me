#!/bin/sh

until sudo python app/main.py; do
    echo "Flask crashed with exit code $?. Restarting..." >&2
    sleep 1
done
