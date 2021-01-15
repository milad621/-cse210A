.PHONY: clean-pyc clean-build docs clean

all:
	pyinstaller main.py

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "(default) - create ARITH language interpreter binary"
	@echo "run - run ARITH language interpreter"

clean: clean-build clean-pyc
	
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	
run:
	python3 main.py