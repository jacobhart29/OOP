# Robot Control Center

## Project Description

My project is a Python program that controls robots. It shows robot information, battery levels, and sensors.

## Features

The program lets you:

* View robots
* Check sensors
* Charge robots
* Reset robot status
* Add sensors
* Exit the program

Run the Python file and enter a command when asked.

## OOP Concepts

* **Classes:** Robot, RobotCar, RobotArm, and Sensor.
* **Constructors:** Create the robots and give them information.
* **Properties:** Check things like battery level and speed.
* **Inheritance:** RobotCar and RobotArm inherit from Robot.
* **Polymorphism:** Different robot types have their own `charge()` method.
* **Composition:** Robots can have sensors.
* **Magic Method:** `__str__()` displays robot information.

## Testing

I tested:

* Normal commands
* Battery at 0 and 100
* Invalid robot IDs
* Invalid numbers
* Invalid commands

The program gives error messages when the user enters incorrect information.
