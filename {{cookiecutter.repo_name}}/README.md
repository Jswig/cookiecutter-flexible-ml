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
{% endif %}

## Project structure
```

{%- if cookiecutter.package_manager == "conda" -%}
├── environment.yml          <- The conda file for reproducing the analysis    
|                         environment.
{%- elif cookiecutter.package_manager == "pip" %}
├── requirements.txt         <- The requirements file for reproducing the analysis 
|                               environment.
{%- endif %} 
{% if cookiecutter.license != "No license file" -%}
├── LICENSE
{%- endif %}
├── README.md                <- The top-level README
{%- if cookiecutter.workflow_automation == "Python" %}
├── run.py                   <- script that runs the full analysis
{%- elif cookiecutter.workflow_automation == "Snakemake" %}
├── Snakefile                <- script with options for running the final analysis
{%- elif cookiecutter.workflow_automation == "Make" %}
├── Makefile                 <- script that runs the full analysis
{%- endif %}
├── data
|   ├── interim              <- Intermediate data that has been transformed.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
├── notebooks                <- Jupyter notebooks
├── output             
|   ├── models               <- Serialized models, predictions, model summaries.
|   └── visualization        <- Graphics created during analysis.
{%- if cookiecutter.project_report == "Yes" %}
├── reports                  <- Generated analysis as HTML, PDF, LaTeX, etc.
{%- endif %}
└── src                      <- Source code for this project.
{%- if cookiecutter.src_structure == "Less" %}
    └── __init__.py          <- Makes this a python module.
{%- elif cookiecutter.src_structure == "More" %}
    ├── __init__.py          <- Makes this a python module.
    ├── data                 <- Scripts to download or generate data.
    |   └── make_dataset.py  
    ├── features             <- Scripts to turn raw data into features for modeling.
    |   └── build_features.py  
    ├── models               <- Scripts used to generate models and inference results.
    └── visualization        <- Scripts to generate graphics
        └── visualize.py
{%- endif %}
```
    
{% if cookiecutter.license != "No license file" -%}
## License

This project is distributed under the  {{ cookiecutter.license }} license.
{%- endif %}