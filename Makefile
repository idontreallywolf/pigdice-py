#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

# path to source files
SRC = ./src

# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-all: clean clean-doc
	rm -rf .venv

# ---------------------------------------------------------
# Test all the code at once.
#
pylint:
	pylint $(SRC)

flake8:
	flake8 $(SRC)

lint: flake8 pylint

.PHONY: test

test:
	$(MAKE) pylint
	$(MAKE) flake8
	coverage run -m unittest discover
	coverage report

run:
	python ./src/main.py

# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	# This does not work on Windows installed Python
	$(PYTHON) -m pydoc -w "$(PWD)"
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	pdoc -o doc/api $(SRC)

pyreverse:
	install -d doc/uml
	pyreverse $(SRC)
	dot -Tpng classes.dot -o doc/uml/classes.png
	dot -Tpng packages.dot -o doc/uml/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx

# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average .

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show .

radon-raw:
	@$(call MESSAGE,$@)
	radon raw .

radon-hal:
	@$(call MESSAGE,$@)
	radon hal .
