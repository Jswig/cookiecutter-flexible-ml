# {{ cookiecutter.project_name }}

*{{ cookiecutter.author_name }}, {% now 'local', '%d/%m/%Y' %}*

{{ cookiecutter.description }}

## Setup

{% if cookiecutter.package_manager == "conda" %}
Create a conda environment with all the required packages: 
```
conda env create -f environment.yml
```
Switch to the new environment:
```
conda activate {{cookiecutter.repo_name}}
```

{% elif cookiecutter.package_manager == "pip" %}
Create an isolated environment using your preferred solution 
(`venv`, `pipenv`,...) and install the required package: 
```
pip install -r requirements.txt
```
{% endif %}


## Project structure

```
.
├── environment.yml    <- File specifying a conda environment
├── LICENSE
├── README.md
├── run.py             <- Script for installing environments and reproducing 
│                         the full analysis
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks
├── output             
└── src                <- Source code for this project
    ├── __init__.py    <- Makes this a python module
```    

{% if cookiecutter.license != "No license" %}
## License

Distributed under the  {{ cookiecutter.license }} license.
{% endif %}