Changelog
=========


0.7.0 (2023-11-29)
------------------

New
~~~
- Added changes to footer, navbar, and testing to finalize for project.
  [Donald McLaughlin]
- Added template images. [Donald McLaughlin]
- Readme template. [Donald McLaughlin]
- Added B_5 buttons over links. [Donald McLaughlin]
- Worked on testing. [Donald McLaughlin]
- Added license. [Donald McLaughlin]
- Update build script. [Donald McLaughlin]
- Added branch v0.7.0. [Donald McLaughlin]
- New: New tag for feats @ v0.6.5. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Update readme. [Donald McLaughlin]
- Added more fixes. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: clean readme. [Donald McLaughlin]
- Update db. [Donald McLaughlin]
- Rename LICENSE.md to LICENSE. [don1997]
- Rename LICENSE to LICENSE.md. [don1997]
- Create LICENSE. [don1997]
- Remove license. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]


0.6.5 (2023-11-28)
------------------

New
~~~
- Added tags and searching for tags. As well as displaying tags in
  template and Search results for tag. [Donald McLaughlin]
- New feats below. [Donald McLaughlin]
- Flesh out unit testing for integration testing, form testing, smoke
  testing, auth-encrypt testing. [Donald McLaughlin]
- Fixed smoke test to work now. Added test-script.py for script exec.
  [Donald McLaughlin]
- Removed dummy search and updated wtf search with bootstrap5. As well
  as removing old tests and adding testing script. [Donald McLaughlin]
- Started to successfully flesh out unit testing. [Donald McLaughlin]
- Trimmed codemirror5_dupe. [Donald McLaughlin]
- Removed codemirror5 (100mb) from submodules and in place made a much
  smaller local file. [Donald McLaughlin]
- Added Gruvbox theme and fixed issue with non tagged element color.
  [Donald McLaughlin]
- Added syntax highlighting based on snippet.title file extension. Now
  supports any lang with file extension. [Donald McLaughlin]
- Added Feats searching, Front end clean up. [Donald McLaughlin]
- Added Search query feature and corresponding form and front end stuff.
  [Donald McLaughlin]
- Added dummy search bar. [Donald McLaughlin]
- Added delete modal and buttons for ops. [Donald McLaughlin]
- Added latest ver of Bootstrap 5.2->5.3, Added scroll for overflow if
  not posted already, work on delete modal. [Donald McLaughlin]
- Added code mirror to new snippet and fixed 4 line space. [Donald
  McLaughlin]
- Added codemirror and a workable edit box in edit_snippet as well as
  copy button and bootstrap stuff. [Donald McLaughlin]
- Added bootstrap 5 css and js and comment out bootstrap 2.x in
  my_base.html. [Donald McLaughlin]
- Added branch v0.6.0_Bootstrap5 for Migrating app to Bootstrap5.
  [Donald McLaughlin]
- New: Added merged changes from tasks @ v0.6.3. [Donald McLaughlin]

Fix
~~~
- Finally fixed db overwrite issue with testing. [Donald McLaughlin]
- Fixed db. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Tagging feat. [Donald McLaughlin]
- Fixed more issues with login testing and added more. [Donald
  McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Fix footer pos and attempt fixed sidebar. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Workign edit snippet codemirror. [Donald McLaughlin]


0.6.3 (2023-11-22)
------------------

New
~~~
- Merged files/changes for testing and error handling tasks. [Donald
  McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]


0.6.2 (2023-11-22)
------------------

New
~~~
- Fixed db model for snippet removed unique constraint as well as made
  fresh db and migrations/ [Donald McLaughlin]
- Added a whole host of things to front end including templates, css,
  boostrap components, and proper links for ops,syntax highlighting,
  forms modifications,  Now has usable front end. [Donald McLaughlin]
- Added tag models. [Donald McLaughlin]
- Added Flask-Bootstrap macro to login successfully. [Donald McLaughlin]
- Added my_base.html template and begin using bootstrap templating into
  project. [Donald McLaughlin]
- Added my_base.html template and begin using bootstrap templating into
  project. [Donald McLaughlin]
- Added flask-bootstrap, Created base.html, and updated main templates.
  [Donald McLaughlin]
- Started fleshing out front-end dirs. [Donald McLaughlin]
- Moved to v0.6.0 for next set of feats. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Fixed Edit_snippet dupes, Cleaned dirs and files, Fixed flashing to
  work. [Donald McLaughlin]
- Working copy. [Donald McLaughlin]
- Added snippet. [Donald McLaughlin]
- Fixed duplicate names in new_snippet. [Donald McLaughlin]
- Attempt to get alembic to work. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Found error and edit forms. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Fixed some front stuff. [Donald McLaughlin]
- Fixed flickering boostrap and css. [Donald McLaughlin]
- Working dash. [Donald McLaughlin]
- Success! Alembic migration worked! [Donald McLaughlin]
- Working on syntax highlight feat and dashboard struct. [Donald
  McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Change: updated scripts: [Donald McLaughlin]


0.6.0 (2023-11-17)
------------------

New
~~~
- Added more unit test stuff and venv script. [Donald McLaughlin]
- Added unit tests for login and conftest changes. [Donald McLaughlin]
- More test. [Donald McLaughlin]
- Added Unit testing and some of the setup for it. [Donald McLaughlin]

Fix
~~~
- Removed Greenlet from requirements.txt. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: New changes to changelog. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]


0.5.0 (2023-11-12)
------------------

New
~~~
- Removed old files from refactor. [Donald McLaughlin]
- Correctly updated src/ this time with refactored changes. [Donald
  McLaughlin]
- Refactored into folders starting with src/. Added Blueprints to routes
  and templates. > Delete old app.py and database.db. Update build
  scripts. [Donald McLaughlin]
- Added resources. [Donald McLaughlin]
- Added branch v0.5.0. [Donald McLaughlin]
- Added Skel for refactor. [Donald McLaughlin]

Fix
~~~
- Added some login_req decorators and more security around crud ops.
  [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Test. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: fix tut. [Donald McLaughlin]
- Chore: fix tut. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Test: build script. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Test: Alright should work this time. [Donald McLaughlin]
- Test: test build.sh to see whether it updates changelog. [Donald
  McLaughlin]
- Chore: Add img/ for present. [Donald McLaughlin]
- Chore: Update README.md. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: add tag 0.4.0. [Donald McLaughlin]


0.4.0 (2023-10-30)
------------------

New
~~~
- Added delete and edit snippet ops with corresponding templates.
  [Donald McLaughlin]
- Added buttons /teamplates in to navigate easier between /snippet/new
  and /dashboard. [Donald McLaughlin]
- Added specific user/id to dashboard.html as well as list all snippets
  associated with user feat. [Donald McLaughlin]
- Added snippet forms. Added routes in /dashboard to perform query on
  snippets. Added startup.sh for startup so i don't have to keep
  creating virtual environments! [Donald McLaughlin]
- Build script test! [Donald McLaughlin]
- Added intermediate of snippet form with tempalte. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cleaned out __pycache/ and test.html. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: cl. [Donald McLaughlin]
- Chore: tag v0.3.0 and cl. [Donald McLaughlin]


0.3.0 (2023-10-28)
------------------

New
~~~
- Added Model for Snippet, Added user-snippet relation, Added Flask-
  Migrate, Change: Migrated db for new models, Test: Entered in
  username=test1 (id=2) for testing in flask shell NOTE: contains plain
  text password! [Donald McLaughlin]

Other
~~~~~
- Chore: Update README. [Donald McLaughlin]
- Chore: add startup steps. [Donald McLaughlin]
- Chore: tags, cl. [Donald McLaughlin]


0.2.0 (2023-10-26)
------------------

New
~~~
- Add User-auth, req.txt, .gitignore for venv, new templates for login
  forms. [Donald McLaughlin]
- Basic Routing and templates for user auth. [Donald McLaughlin]

Other
~~~~~
- Chore: cl. [Donald McLaughlin]
- Change: Cleaned up old code, old uneeded files to make way for new
  v0.1.0. [Donald McLaughlin]
- Chore: Added branches and cl. [Donald McLaughlin]


0.1.0 (2023-10-26)
------------------
- Chore: cl. [Donald McLaughlin]


00.00.10 (2023-10-26)
---------------------

New
~~~
- Added pytest Unit testing to app. [Donald McLaughlin]
- View code and entry form in browser. [Donald McLaughlin]

Other
~~~~~
- Chore: C.L. [Donald McLaughlin]
- Chore: changelog. [Donald McLaughlin]
- Chore: Readme. [Donald McLaughlin]
- Chore: Update readme for steps on tagging. [Donald McLaughlin]
- Test: update changeloggit add .git add . [Donald McLaughlin]
- Test: again. [Donald McLaughlin]


00.00.03 (2023-10-24)
---------------------

New
~~~
- Added delete and fixed issues with prev crud ops. [Donald McLaughlin]
- Introduce SQL Alchemy to application, Create SQL Lite DB for test,
  Added crud ops. In progress: Add delete feature with respective
  template. [Donald McLaughlin]
- Pulls from boostrap template. [Donald McLaughlin]
- Add template test and flask-bootstrap Chore: Added commit syntax in
  README. [Donald McLaughlin]
- Introduced gitignore to repo. Added: CHANGELOG.md, initial project
  tag. [Donald McLaughlin]

Fix
~~~
- Fixed readme snippet. [Donald McLaughlin]

Other
~~~~~
- Test: test. [Donald McLaughlin]
- Test: test log. [Donald McLaughlin]
- Chore: attempt to fix tags and changelog. [Donald McLaughlin]
- Chore: Redo tree. [Donald McLaughlin]
- Chore: replant tree. [Donald McLaughlin]
- Chore: add tree. [Donald McLaughlin]
- Chore: Update README. [Donald McLaughlin]
- Chore: update log. [Donald McLaughlin]
- Chore: Added todo README. [Donald McLaughlin]
- Chore: test for ssh compat and update changelog. [Donald McLaughlin]
- Updated changelog. [Donald McLaughlin]
- Docs: Repo Changelog update. [Donald McLaughlin]
- Docs: added testing command. [Donald McLaughlin]
- Chore: fixed tag to intended message. [Donald McLaughlin]
- Modify readme. [Donald McLaughlin]
- Added dummy txt files to fix missing empty folders. [Donald
  McLaughlin]
- Added test. [Donald McLaughlin]
- Added skeleton. [Donald McLaughlin]


