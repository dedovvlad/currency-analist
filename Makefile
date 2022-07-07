tests:
	pytest test/ -v -s

linters:
	isort src/
	isort test/
	black src/ --line-length=100
	black test/ --line-length=100