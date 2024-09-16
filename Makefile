
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./python_files

lint:
# pylint ./python_files/desc_stats_main.py
	ruff check ./python_files/*.py  ./python_files/*.ipynb 
# ruff ./*.py
	
test:
# python -m pytest /python_files/tests/test_desc_stats.py
	python -m pytest test_*.py *.ipynb

check:
	python desc_stats_main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \

deploy:
	#deploy goes here

all: install lint format test 