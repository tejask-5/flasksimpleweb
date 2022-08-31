#!/bin/bash

date >> output.log
whoami >> output.log
pwd >> output.log
FLASK_APP=app.py  FLASK_ENV=development  /home/seahk/anaconda3/bin/flask  run  --port 8001  --host=0.0.0.0
