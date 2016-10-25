# Bank Simulator

[![Build Status](https://travis-ci.org/DDiPuma/bankSimulator.svg?branch=master)](https://travis-ci.org/DDiPuma/bankSimulator)

This project contains the following:
- Raw .dia files for UML diagrams of the system's design
- Readable .png files of the design artifacts
- Source files for the implementation of the design
- Source files for unit, integration, system, and acceptance tests, to be run via pytest on Travis-CI's servers
- A source file for a main method which executes the example assigned (10 turns of 10 customers, for 1..10 tellers) and generates a graph via matplotlib
- A .png of the graph produced by main

Dependencies:
- Python 3.x (might run on 2.x, but it is unsupported)
- pytest (runs tests and integrates cleanly with Travis-CI)
- matplotlib
