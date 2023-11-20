# CSM v0.6.0 
## Note: Fix build scripts

## gitchangelog 
    New: for introducing a new feature.
    Fix: for a bug fix.
    Change: for a change in existing functionality.
    Docs: for documentation updates.
    Style: for code formatting, missing semi-colons, etc.
    Refactor: for refactoring code.
    Test: for adding or updating tests.
    Chore: for housekeeping tasks, e.g., updating the build process.

-----

### Branching stuff
- create branch
git branch <branch_name or vx.x.x>

- switch
git checkout vx.x.x

- create and switch to new branch
git checkout -b vx.x.x

- View all branches.
git branch -a
### Steps to add tag
git tag -a 00.00.01 -m 'my version 1.0' NOTE: DO NOT USE 'vxx.xx.xx'  

git push origin --tags

gitchangelog > CHANGELOG.md

### Goal
Create prototyp with the following features:
* User auth x
* DB Design and CRUD X 
* user-snippet relationship X
* Basic front end app to put it all together. x

---

### Startup Steps
1. clone repo
2. cd into cloned repo
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. flask run
7. deactivate #to turn off venv!
### Merge branch
once feature works!
git checkout master #switch to master
git merge v0.1.0 #merge v0.1.0 to master
git push origin master #push changes!

### TODO When moving to next phase
* Update build script to reflect branch to submit to.
### PLAN next

BACKEND
1. Refactor Backend into Lib x
2. Add Documentation while refactor
3. Implement Next App feats
    * Search ~ 
    * Tags
4. Add Unit testing x
5. Windows run and scripts x
6. Look into adding docker to prototype build
FRONTEND

1. Bootstrap learn x
2. Js front end

## Using Alembic

1. Ensure path to project is correct in this case: $ export FLASK_APP=src/run.py

2. $ flask db migrate -m "Your feature description"
3. flask db upgrade

