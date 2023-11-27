"""
A simple repl used for executing scripts.

Note: build.sh, venv.sh not sure hwo those work. dont mess with 
"""

import subprocess
import glob
import os

def list_shell_scripts(directory):
    # List all .sh files in the specified directory
    return glob.glob(os.path.join("/home/donald/Projects/csm/", '*.sh'))



def run_script(script_path):
    try:
        subprocess.call("/home/donald/Projects/csm/" + script_path)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}:\n{e}")

def repl():
    while True:
        scripts = list_shell_scripts("/home/donald/Projects/csm/",)
        print("Available Scripts:")
        for script in scripts:
            print(f"  - {os.path.basename(script)}")

        script_name = input("Enter script to run (or 'exit' to quit): ")
        if script_name.lower() == 'exit':
            break
        run_script(script_name)

if __name__ == "__main__":
    repl()


