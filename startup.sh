#!/bin/bash

#Nav to project dir (Change if located somewhere else!)
cd /home/donald/Projects/csm

source venv/bin/activate

python3 src/run.py

deactivate

echo "Run Successful!"
