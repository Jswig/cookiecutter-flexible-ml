import os
import shutil

os_license = '{{ cookiecutter.license }}'
package_manager = '{{ cookiecutter.package_manager }}'
workflow_automation = '{{ cookiecutter.workflow_automation }}'

if os_license == "No license file":
    os.remove("LICENSE")

if package_manager == "conda":
    os.remove("environment.yml")
elif package_manager == "pip":
    os.remove("requirements.txt")

if workflow_automation == "Python":
    os.remove("Makefile")
    os.remove("Snakefile")
elif workflow_automation == "Make":
    os.remove("run.py")
    os.remove("Snakefile")
elif workflow_automation == "Snakemake":
    os.remove("Makefile")
    os.remove("run.py")