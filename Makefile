PHONY: check
check:
	black .
	isort .
	flake8 .
