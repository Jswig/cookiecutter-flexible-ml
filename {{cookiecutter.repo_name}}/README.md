# {{ cookiecutter.project_name }}

*{{ cookiecutter.author_name }}, {% now 'local', '%d/%m/%Y' %}*

{{ cookiecutter.description }}

## Setup

{% if cookiecutter.package_manager == "conda" -%}
Create a conda environment with all the required packages: 
```
conda env create -f environment.yml
```
Switch to the new environment:
```
conda activate {{cookiecutter.repo_name}}
```
{% elif cookiecutter.package_manager == "pip" -%}
Create an isolated environment using your preferred solution 
(`venv`, `pipenv`,...) and install the required package: 
```
pip install -r requirements.txt
```
{% endif -%}

## Project structure
    
{% if cookiecutter.license != "No license file" -%}
## License

This project is distributed under the  {{ cookiecutter.license }} license.
{%- endif %}