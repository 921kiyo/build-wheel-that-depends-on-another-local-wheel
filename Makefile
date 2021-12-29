package:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist pip-wheel-metadata .mypy_cache .pytest_cache
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +