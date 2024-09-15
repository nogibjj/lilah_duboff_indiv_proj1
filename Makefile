python_files_var = desc_stats.py test_desc_stats.py
notebook_files_var = *.ipynb

.PHONY: install test format lint

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint /python_files/desc_stats.py
	ruff $(python_files_var)

test:
	python pytest /python_files/tests/test_desc_stats.py
	jupyter nbconvert --to notebook --execute $(notebook_files_var) --inplace

all: install lint test


	

