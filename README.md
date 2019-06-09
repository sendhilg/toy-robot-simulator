# Toy Robot Simulator

## Description
The application is completed as a task following the requirements in [brief](BRIEF.md).

## Requirements
The application was developed using python version 3.7.3

To check the version on your machine run the below command:

    $ python --version

## Running the application
Clone the project from github. Change into the project directory toy_robot_simulator.

The application can either accept inputs from the command line or from an input file.

To accept input from the command line, type the below, press enter and start entering commands:

    $ python toy_robot

To accept input from an input file, create input file with the commands, type the below and press enter:

    $ cat /path/to/input_file | python toy_robot

Following commands are accepted at the command line. 
* `PLACE X,Y,FACING` will put the toy robot on the table in position X,Y and the facing direction.
* `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
* `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction.
* `REPORT` will print the X,Y and FACING of the robot.

### Examples
```
a)
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH

b)
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
```

## Unit Tests

### Prerequisites
pytest library is required for running the application's unit tests. Install pytest. Also optionally install pytest-cov if the code coverage needs to be checked.

    $ pip install pytest
    $ pip install pytest-cov

### Running unit tests
Navigate to the repository and run the below command to run the tests.

    $ pytest

Navigate to the repository and run the below command to run
the tests displaying code coverage.

    $ pytest --cov=toy_robot tests/
