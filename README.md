# Bank Simulator

[![Build Status](https://travis-ci.org/DDiPuma/bankSimulator.svg?branch=master)](https://travis-ci.org/DDiPuma/bankSimulator)

This project contains the following:
- design/ - design diagrams in .png format
- design/artifacts/ - design diagrams in raw .dia format
- src/ - implementation of the design
- src/main.py - driver to execute the design and produce a graph
- test/ - unit, integration, and system and acceptance tests to be run via pytest on Travis-CI

Dependencies:
- Python 3.x (might run on 2.x, but it is unsupported)
- pytest (runs tests and integrates cleanly with Travis-CI)
- matplotlib

The example software can be run with 'python src/main.py' in this folder, or
'python3 src/main.py', depending on which Python version is installed and 
linked. matplotlib must be installed for Python 3. Some unit tests need pytest
to execute, and pytest is the most efficient way to run all the tests at once.
