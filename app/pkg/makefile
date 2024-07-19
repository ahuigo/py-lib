test:
	python3 -m pytest -s

PHONY: tests
tests:
	python -m tests.test_client
	PYTHONPATH=. python tests/test_client.py

# how to create a new project?
# 1. create project package
create:
	poetry new mypkg
