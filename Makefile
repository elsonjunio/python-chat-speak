#Makefile
.PHONY: install format lint test sec

install:
	@poetry install
format:
	@blue .
	@isort .
lint:
	@blue --check .
	@isort --check .
	@prospector
test:
	@python test/first_test.py
	@coverage run --source ./ -m unittest discover -p "*_test.py" && coverage report
sec:
	@pip-audit