PYTHON ?= python3

.PHONY: build check test verify
build:
	$(PYTHON) scripts/catalog.py build
check:
	$(PYTHON) scripts/catalog.py check
test:
	$(PYTHON) -m unittest discover -s tests -v
verify: check test
