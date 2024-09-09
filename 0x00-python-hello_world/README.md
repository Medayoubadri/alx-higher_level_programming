# Project: 0x00. Python - Hello, World

## Description
This project focuses on the basics of Python programming, covering fundamental concepts such as printing, string manipulation, compiling Python files, and reverse-engineering Python bytecode. You will also learn how to write shell scripts that interact with Python files and how to check for cycles in a singly linked list.

---

## Table of Contents
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Run Python file](#task-0-run-python-file)
  - [Task 1: Run inline](#task-1-run-inline)
  - [Task 2: Hello, print](#task-2-hello-print)
  - [Task 3: Print integer](#task-3-print-integer)
  - [Task 4: Print float](#task-4-print-float)
  - [Task 5: Print string](#task-5-print-string)
  - [Task 6: Play with strings](#task-6-play-with-strings)
  - [Task 7: Edges of a string](#task-7-edges-of-a-string)
  - [Task 8: Concatenate strings](#task-8-concatenate-strings)
  - [Task 9: Easter Egg](#task-9-easter-egg)
  - [Task 10: Check for cycles](#task-10-check-for-cycles)
  - [Task 11: Write to stderr](#task-11-write-to-stderr)
  - [Task 12: Compile Python script](#task-12-compile-python-script)
  - [Task 13: Bytecode to Python](#task-13-bytecode-to-python)

---

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Shell Scripts
- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable

### C Scripts
- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded

---

## Tasks

### Task 0: Run Python file
**File**: `0-run`

Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

### Task 1: Run inline
**File**: `1-run_inline`

Write a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`.

### Task 2: Hello, print
**File**: `2-print.py`

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle"`, followed by a new line.

### Task 3: Print integer
**File**: `3-print_number.py`

Write a Python script that prints the integer stored in the variable `number`, followed by `"Battery street"`, and a new line.

### Task 4: Print float
**File**: `4-print_float.py`

Write a Python script that prints the float stored in the variable `number` with a precision of 2 digits.

### Task 5: Print string
**File**: `5-print_string.py`

Write a Python script that prints 3 times a string stored in the variable `str`, followed by its first 9 characters.

### Task 6: Play with strings
**File**: `6-concat.py`

Write a Python script that concatenates two strings, `str1` and `str2`.

### Task 7: Edges of a string
**File**: `7-edges.py`

Write a Python script that manipulates and prints specific parts of a string.

### Task 8: Concatenate strings
**File**: `8-concat_edges.py`

Write a Python script that prints the specific string: `"object-oriented programming with Python"`.

### Task 9: Easter Egg
**File**: `9-easter_egg.py`

Write a Python script that prints `"The Zen of Python"`, by Tim Peters.

### Task 10: Check for cycles
**File**: `10-check_cycle.c`

Write a C function that checks if a singly linked list has a cycle in it.

### Task 11: Write to stderr
**File**: `100-write.py`

Write a Python script that prints exactly `"and that piece of art is useful - Dora Korpar, 2015-10-19"`, followed by a new line, to the standard error.

### Task 12: Compile Python script
**File**: `101-compile`

Write a Shell script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`.

### Task 13: Bytecode to Python
**File**: `102-magic_calculation.py`

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the provided Python bytecode.

---

### This README was compiled without any help from Stack Overflow... Okay, maybe just a little bit.

