# CSM v0.1.0 

```bash
$ flask run
```
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
* DB Design and CRUD 
* user-snippet relationship
* Basic front end app to put it all together.

---

### Startup Steps
1. clone repo
2. cd into cloned repo
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. flask run
