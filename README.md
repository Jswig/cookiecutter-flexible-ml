# Cookiecutter Flexible ML

![Python version](https://img.shields.io/badge/Python-3.x-informational)
![Issues closed](https://img.shields.io/github/issues-closed/Jswig/cookiecutter-flexible-ml)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

*Anders Poirel*

A flexible cookiecutter template for reproducible data science.
`cookiecutter` is a command-line utility that creates projects from 
cookiecutters (project templates). See
[cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io/en/1.7.0/index.html).

## ⚙ Usage

*Requirements*:
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/min) >= 1.1

Run
```bash
cookiecutter gh:Jswig/cookiecutter-flexible-ml
```

`[Enter]` will select the default option in prompt.


## 📁 Generated project structure

Some of these might not be created depending on options picked
```
.
├── LICENSE
├── environment.yml /  <- File specifying an environment
|   requirements.txt   
├── README.md
├── run.py/Makefile    <- Script for running the full
|    /Snakefile          analysis.
│                        
├── data
|   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling. 
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks.
├── output             <- For outputs of running the analysis.
│   ├── models         <- Saved models and predictions.      
│   └── visualizations <- Graphics created during analysis.       
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
└── src                <- Source code for this project.
    └── __init__.py    <- Makes this a Python module.
```    

## ✅ Motivation

A project template that promotes good practices for reproducible 
data science (immutablity of raw data, seperation of exploratory code and 
"final" analysis code), while giving options for more or less complex projects

 - A python script is used by default for workflow automation instead of
  a `Makefile` (though it is left as an option) to avoid issues for Windows 
  users. `snakemake` is preferred for "real" projects.
 - The template does not include boilerplate for generating documentation or 
 python packages, which is not necessary for the intended use case of personal
 /classroom projects.
 
This project is meant to adapt (and borrows liberally from) Driven Data's 
[cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science#keep-secrets-and-configuration-out-of-version-control).
structure and philosophy to slightly different needs.


##  License

This project is distributed under the [MIT License](https://github.com/Jswig/cookiecutter-minimal-ml/blob/master/LICENSE).
