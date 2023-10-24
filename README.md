# CSM

## Testing
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
 
### Todo
- Fix Version tag
- Fix changelog
- Add install scripts for pip stuff
- Add demo instructions with pics/gif?

----

```
.
├── app.py
├── CHANGELOG.md
├── instance
│   └── project.db
├── __pycache__
│   └── app.cpython-310.pyc
├── README.md
├── static
│   └── dummy.txt
└── templates
    ├── base.html
    ├── my_template.html
    ├── test.txt
    ├── user_create.html
    ├── user_delete.html
    ├── user_detail.html
    └── user_list.html

4 directories, 13 files
```
---- 

### Steps to add tag
git tag -a 00.00.01 -m 'my version 1.0' NOTE: DO NOT USE 'vxx.xx.xx'  
git push origin --tags
gitchangelog > CHANGELOG.md
