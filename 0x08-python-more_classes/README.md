
# **0x08. Python - More Classes and Objects**

## **Project Overview**

This repository contains various Python classes and programs focusing on **classes, objects**, and a sprinkling of advanced **object-oriented programming** concepts. In particular, we dealt with **geometry** (rectangles, to be precise) and took on the challenge of solving the **N-Queens problem**—one of the classics of computer science and chessboard acrobatics.

## **Table of Contents**
1. [General Information](#general-information)
2. [Requirements](#requirements)
3. [Project Files](#project-files)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Authors](#authors)
7. [Random Fun Fact](#random-fun-fact)

## **General Information**

Throughout this project, you will:
- Implement several **Python classes** to define and manage **rectangles** with attributes like width, height, and the ability to **calculate area and perimeter**.
- Explore the concepts of **public and private attributes**, **property decorators**, **class and static methods**, and **object representation**.
- Write a Python program that solves the **N-Queens** problem, using **backtracking** to determine valid queen placements on an NxN chessboard.

## **Requirements**

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 **version 3.8.5**
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle **version 2.8.***
- All your files must be executable
- The length of your files will be tested using `wc`.

## **Tasks**

### Task 0: Simple Rectangle
- **File**: `0-rectangle.py`
- **Description**: Create an empty class `Rectangle` that defines a rectangle.

### Task 1: Real Definition of a Rectangle
- **File**: `1-rectangle.py`
- **Description**: Add `width` and `height` attributes with validation to define a rectangle. Properties `width` and `height` use setters for validation.

### Task 2: Area and Perimeter
- **File**: `2-rectangle.py`
- **Description**: Add methods to compute the area and perimeter of the rectangle. If either `width` or `height` is zero, perimeter is `0`.

### Task 3: String Representation
- **File**: `3-rectangle.py`
- **Description**: Implement the `__str__` method to print the rectangle using the `#` character.

### Task 4: Eval is Magic
- **File**: `4-rectangle.py`
- **Description**: Add the `__repr__` method to provide a string representation that can recreate the object using `eval()`.

### Task 5: Detect Instance Deletion
- **File**: `5-rectangle.py`
- **Description**: Add the `__del__` method that prints `"Bye rectangle..."` when an instance is deleted.

### Task 6: How Many Instances
- **File**: `6-rectangle.py`
- **Description**: Add a public class attribute `number_of_instances` to keep track of the number of instances created and deleted.

### Task 7: Change Representation
- **File**: `7-rectangle.py`
- **Description**: Add a public class attribute `print_symbol` that allows customization of the symbol used for printing the rectangle.

### Task 8: Compare Rectangles
- **File**: `8-rectangle.py`
- **Description**: Add a static method `bigger_or_equal` that compares two rectangles by area and returns the bigger one.

### Task 9: A Square is a Rectangle
- **File**: `9-rectangle.py`
- **Description**: Add a class method `square` that creates a new `Rectangle` instance where `width` and `height` are equal.

### Task 10: N-Queens Problem
- **File**: `101-nqueens.py`
- **Description**: Solve the N-Queens puzzle for an `N x N` chessboard, using backtracking to find all possible solutions where queens do not threaten each other.

## **Project Files**

### Rectangle Files

| File Name         | Description |
|-------------------|-------------|
| `0-rectangle.py`  | Defines an empty class `Rectangle`. |
| `1-rectangle.py`  | Adds `width` and `height` attributes, with properties for validation. |
| `2-rectangle.py`  | Adds methods to compute the area and perimeter of the rectangle. |
| `3-rectangle.py`  | Adds `__str__` method for string representation using the `#` symbol. |
| `4-rectangle.py`  | Adds `__repr__` method for recreating the instance using `eval()`. |
| `5-rectangle.py`  | Adds `__del__` method that prints a farewell message when the instance is deleted. |
| `6-rectangle.py`  | Adds `number_of_instances` to track how many rectangles exist. |
| `7-rectangle.py`  | Adds `print_symbol` to customize how the rectangle is printed. |
| `8-rectangle.py`  | Adds a static method `bigger_or_equal` to compare rectangles by area. |
| `9-rectangle.py`  | Adds a class method `square` to create a square (i.e., a rectangle with equal width and height). |

### N-Queens Solver

| File Name         | Description |
|-------------------|-------------|
| `101-nqueens.py`  | Solves the N-Queens puzzle using backtracking, printing all possible solutions. |

## **Authors**

**[MedayouBadri](https://github.com/medayoubadri)**

## **Fun Fact**

Did you know?
The N-Queens problem was first posed in 1848 by Max Bezzel, a chess player. Little did he know that programmers around the world would be endlessly battling it out with recursive algorithms to help these queens coexist on a chessboard in peace.