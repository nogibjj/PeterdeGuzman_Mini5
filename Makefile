
install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb

test: 
	python -m pytest -vv --nbval -cov=mylib -cov=main test_lib.py test_main.py *.ipynb

all: install format lint test 




