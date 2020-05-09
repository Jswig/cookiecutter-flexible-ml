# {{ cookiecutter.project_name }}

*{{ cookiecutter.author_name }}, {% now 'local', '%d/%m/%Y' %}*

{{ cookiecutter.description }}

## Installation


## Running the project

```bash
python run.py project
```

If you want to setup and run everything at once, use
```
python run.py 
```

## Project structure

```
.
├── environment.yml    <- File specifying a conda environment
├── LICENSE
├── README.md
├── run.py             <- Script for installing environements and reproducing 
│                         the full analysis
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks
├── output             <- For a manuscript source, e.g., LaTeX, Mark
└── src                <- Source code for this project
    ├── __init__.py    <- Makes this a python module
```    
