PHONY: check
check:
	black .
	flake8 .
	isort .

