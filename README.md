# cookiecutter-flexible-science

*Anders Poirel, May 2020*

A cookiecutter template for simple data science  and machine learnning projects using `conda` for environment management.
For more information on what `cookiecutter` does, check out [cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io/en/1.7.0/index.html).

## Usage

*Requirements*:
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/min) >= 1.40

Run
```bash
cookiecutter gh:Jswig/cookiecutter-minimal-ml
```

If in doubt, I recommend using the default option (Press \[Enter\] at the prompt).

## Motivation

I wanted a simple template that promotes good practices for reproducible data science (immutablity of raw data, seperation of exploratory code and canonical analysis), while allowing 
 - A python script is used by default for workflow automation instead of
  a `Makefile` (though I leave it as an option) to avoid issues for 
  Windows users. `snakemake` is preferred for "real" projects.
 - The template does not include boilerplate for generating 
 documentation or python packages, which is not necessary for my intended
 use case of personal/classroom projects
 


I took heavy insipration from the template and philosophy described by Driven Data at [cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science/#keep-secrets-and-configuration-out-of-version-control).

## Project structure

Som of these are optional
```
.
├── LICENSE
├── environment.yml /  <- File specifying a conda environment
|   requirements.txt   
├── README.md
├── run.py/Makefile    <- Script for installing environments and
|    /Snake file          reproducing  the full analysis.
│                        
├── data
|   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling. 
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks.
├── output             <- For outputs of running the analysis.
│   ├── visualizations <- visualizations generated during the analysis .               
│   └── models         <- Saved models and predictions.
│
└── src                <- Source code for this project.
    └── __init__.py    <- Makes this a Python module.
```    

## License

This project is licensed under the [MIT License](https://github.com/Jswig/cookiecutter-minimal-ml/blob/master/LICENSE).
