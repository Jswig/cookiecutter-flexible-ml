# cookiecutter-minimal-ml

*Anders Poirel, April 2020*

A cookiecutter template for simple data science  and machine learnning projects using `conda` for environment management.
For more information on what `cookiecutter` does, check out [cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io/en/1.7.0/index.html).

## Usage

*Requirements*:
- [conda](https://docs.conda.io/en/latest/miniconda.html) >= 4, and added to your PATH
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/min) >= 1.40

Run
```bash
cookiecutter gh:Jswig/cookiecutter-minimal-ml
```

The user is expected to modify the following skeleton in `run.py` 
```python
def build_project():
    pass
```
to include code for reproducing the full analysis using code defined in `src`: acquiring data, building features, training a the model, making visualization.


## Motivation

I wanted a simple template that promotes good practices for reproducible data science (immutablity of raw data, seperation of exploratory code and canonical analysis) while being easy for beginners in data science to use. 
 - A python script was preferred to a `Makefile` to avoid issues for Windows users. `snakemake` would be preferred for "real" projects.
 - The template does not include boilerplate for generating documentation or python packages, which would not be useful in the assumed use case of simple personal/classroom projects.


I took heavy insipration from the template and philosophy described by Driven Data at [cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science/#keep-secrets-and-configuration-out-of-version-control).

## Project structure

```
.
├── environment.yml    <- File specifying a conda environment
├── LICENSE
├── README.md
├── run.py             <- Script for installing environements and reproducing 
│                         the full analysis.
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks.
├── output             <- For outputs of running the analysis.
│   ├── visualizations <- Visualizations generated during the analysis .               
│   └── models         <- Saved models and predictions.
│
└── src                <- Source code for this project.
    └── __init__.py    <- Makes this a Python module.
```    

## License

This project is licensed under the [MIT License](https://github.com/Jswig/cookiecutter-minimal-ml/blob/master/LICENSE).
