# cookiecutter-minimal-ml

*Anders Poirel*

A cookiecutter template for simple data science  and machine learnning projects using `conda` for environment management.

## Usage

*Requirements*:
- [conda](https://docs.conda.io/en/latest/miniconda.html) >= 4, and added to your PATH
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/min) >= 1.40

Run
```bash
cookiecutter gh:Jswig/cookicutter-minimal-ml
```

The user is expected to modify in `run.py` the following skeleton
```python
def build_project():
    pass
```
to include code for reproducing the full analysis using code defined in `src`: acquiring data, building features, training a the model, making visualization.


## Motivation

I wanted a simple template that promores good practices for reproducible data science (immutablity of raw data, seperation of exploratory code and canonical analysis) for beginners in data science to use:
 - a python script was preferred to a `Makefile` to avoid issues for Windows users. `snakemake` would be preferred for "real" projects
 - the template does not include boilerplate for generating documentation or python packages which aren't useful for the assumed use case of simple personal or classroom projects.


I took heavy instpiration from the [cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science/#keep-secrets-and-configuration-out-of-version-control) template and philosophy. 


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
├── output             <- For outputs of running the analysis
│   ├── visualizations <- Visualization                
│   └── models         <- Saved models and predictions
│
└── src                <- Source code for this project
    └── __init__.py    <- Makes this a python module
```    