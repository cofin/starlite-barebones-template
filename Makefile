docs-clean:
	rm -rf docs/_build

docs-serve:
	sphinx-autobuild docs docs/_build/ -j auto --watch app, tests

docs: docs-clean
	sphinx-build -M html docs docs/_build/ -E -a -j auto --keep-going

test:
	pytest tests
