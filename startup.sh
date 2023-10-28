#!/bin/bash

#Nav to project dir (Change if located somewhere else!)
cd /home/donald/Projects/csm

source venv/bin/activate

flask run

deactivate

echo "Run Successful!"
