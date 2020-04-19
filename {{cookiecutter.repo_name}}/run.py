import subprocess
import sys

# import files from src as needed here

def build_project():
    # your code to run the full analysis here
    pass

def setup():
    subprocess.run([
        "conda env create -f environment.yml",
        "conda activate {{cookiecutter.repo_name}}"
    ])

if __name__ == "__main__":

    if len(sys.argv) == 2:
        choices = {
            'project' : build_project,
            'setup'   : setup
        }
        choices[sys.argv[1]]()
    else:
        setup()
        build_project()