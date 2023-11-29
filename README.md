# CSM v0.7.0 

# Summary
A minimal code snippet manager app written with Python. Using Flask, SQL Alchemy, and Bootstrap.

# Dependencies
* python
* Virtual Environment

# Install and Run

## Linux
1. git clone repo
2. cd into project
3. python3 -m venv venv
4. source venv/bin/activate 
5. pip install -r requirements.txt
6. python3 src/run.py
7. Open a browser with local host opened up.
8. Run app
9. To close ctr+c and deactivate venv.

## Windows
1. git clone repo
2. cd into project 
3. python -m venv venv
4. venv\Scripts\Activate.ps1
5. pip install -r .\requirements.txt
6. python src\run.py
7. Open a browser with local host opened up.
8. Run app
9. To close ctr+c and deactivate venv.

# Testing
This app uses pytest for testing. 
To run all tests simply type `pytest` in the root directory of the project.
To run the smoke test type `pytest -m smoke`
