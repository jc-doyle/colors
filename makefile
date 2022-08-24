# A Python Makefile

# Change if you use 'python' over 'python3'
PYTHON:=python3

# Python module locations
RUN:=src.main

# All are phony cmds
.PHONY: venv install clean run

default: install

venv:
	@echo "Creating virtual environment.."
	test -d venv || $(PYTHON) -m venv --upgrade-deps venv

dependencies: venv
	@echo "Installing packages.."
	. venv/bin/activate; $(PYTHON) -m pip install -Ur requirements.txt

install: dependencies
	@echo "Installing packages.."
	. venv/bin/activate; $(PYTHON) -m pip install --editable .

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
