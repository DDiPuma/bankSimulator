# Bank Simulator

![Travis-CI Status Image](https://travis-ci.org/DDiPuma/bankSimulator.svg?branch=master)

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

Note as well that there are some quirks to the design which might require explanation:
- At this point, the simulation system is interfaced with via external Python code, such as the main.py class offered here.  The system's interface was designed to be easy to work with, and it is possible to implement a simple console UI for the system if the customer wants an interactive simulator.  However, the customer's use case doesn't require this.
- The Event and EventAnalyzer architecture is designed to be loosely coupled, so that it can be repurposed for other simulators
- There are three types of Events in the bank simulator -- however, it is only necessary (at least for now...) to pull metrics from the final type of event, which is the CustomerDepartureEvent, and reflects the wait time and total time spent in the bank
- The modularity of the architecture allows for the other event types to be analyzed, and even for new event types to be added upon customer request
