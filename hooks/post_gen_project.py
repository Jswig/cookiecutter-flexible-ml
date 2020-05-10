import os
import shutil

os_license = '{{ cookiecutter.license }}'
package_manager = '{{ cookiecutter.package_manager }}'
workflow_automation = '{{ cookiecutter.workflow_automation }}'
project_report = '{{ cookiecutter.project_report }}'

if os_license == "No license file":
    os.remove("LICENSE")

if package_manager == "conda":
    os.remove("requirements.txt")
elif package_manager == "pip":
    os.remove("environment.yml")

if workflow_automation == "Python":
    os.remove("Makefile")
    os.remove("Snakefile")
elif workflow_automation == "Make":
    os.remove("run.py")
    os.remove("Snakefile")
elif workflow_automation == "Snakemake":
    os.remove("Makefile")
    os.remove("run.py")