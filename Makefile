#!/bin/bash

check-requirements:
	pip3 freeze > requirements.txt

requirements: check-requirements
	pip3 install -r requirements.txt

run: requirements
	python3 main.py

tests: requirements
	python3 -m pytest tests/

clean:
	rm -r __pycache__