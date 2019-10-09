SHELL := /bin/bash

venv:
	virtualenv -p python3.6 ./venv

init: 
	source venv//bin/activate; \
    pip install -r requirements.txt; \

test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox

ci:
	pytest -v tests/

flake8:
	flake8 --ignore=E501,F401,E128,E402,E731,F821 hwsdk

coverage:
	pytest --verbose --cov-report term --cov-report xml --cov=hwsdk tests

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
#     twine upload --repository testpypi dist/*
	rm -fr build dist .egg hwsdk.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
