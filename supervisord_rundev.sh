#!/bin/bash

# supervisord fails to kill the dev servers it spawns,
# make sure they're all dead before starting a new one.
/usr/local/vegphilly/killdev.py 8000
/usr/local/vegphilly/manage.py runserver 0.0.0.0:8000
