#!/bin/bash

#check for commit message
if [ "$#" -ne 1 ]; then
    echo "Usage: ./build.sh <commit_message>"
    exit 1
fi

# commit to var
commit_message=$1

#Nav to project dir (Change if located somewhere else!)
cd /home/donald/Projects/csm

#avoid conflicts!
git pull origin v0.5.0

#update changelog
gitchangelog > CHANGELOG.md

# Add
git add .

# Commit!
git commit -m "$commit_message"

git push origin v0.5.0

echo "Pushed to GitHub successfully!"

# For updating changelog since changelog updates are only visible after the 
# the commit has taken place

#update changelog to see commit 
gitchangelog > CHANGELOG.md

git add .

git commit -m "Chore: cl"

git push origin v0.5.0

echo "Changelog updated Successfully!"
