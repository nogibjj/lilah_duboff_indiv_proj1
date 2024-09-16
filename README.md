[![Python Application Test with Github Actions](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/format.yml)

[![Python Application Test with Github Actions](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/install.yml)

[![Python Application Test with Github Actions](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/lint.yml)

[![Python Application Test with Github Actions](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_indiv_proj1/actions/workflows/test.yml)

# **Individual Project 1: Pandas Descriptive Statistics**
##### The goal of this project is to utilize pandas to create summary statistics and visualizations for a data set
#### Requirements:

- [x] Jupyter Notebook with: 
    - Cells that perform descriptive statistics using Polars or Panda.
    - Tested by using nbval plugin for pytest
- [x] Makefile with the following:
    - Run all tests (must test notebook and script and lib)
    - Formats code with Python black Links to an external site.
    - Lints code with Ruff Links to an external site.
    - Installs code via:  pip install -r requirements.txt
- [x] test_script.py to test script
- [x] test_lib.py to test library
- [x] Pinned requirements.txt
- [x] Gitlab Actions performs all four Makefile commands with badges for each one in the README.md

---
### Project Video 
------------
<insert video link>

### Workflow Summary and Explanation
---
##### This project contains the following dependencies:
- pylint 
- black
- pytest
- pandas
- matplotlib
- jupyter
- ruff 
- nbval 
- tabulate 

---
### Folder Navigation
---
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - workflows
            - main.yml
            - OTHER YAMLS
    - data
        - us_driving_fatalities.csv
    - python files
        - tests
            - test_desc_stats.py
            - test_lib.py
        - desc_stats.py
        - lib.py
    - Makefile
    - README.md
    - requirements.txt
---
### Descriptive Statistics Table
---
###### The following table is the desc_stats.py/jupyter output, indicating the count, mean, std, min, quartiles, and max for the numeric variables


---
### Visualizations
---
###### The following graph is a visualization created by the script, which displays a comparison of the number of driving fatalities per year reported in the dataset

![alt text](python_files/outputs/output.png)







