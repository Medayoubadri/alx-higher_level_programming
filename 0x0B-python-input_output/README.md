# 0x0B. Python - Input/Output

This project covers various tasks related to file handling and input/output operations in Python. 
It involves reading from and writing to files, manipulating file contents, and working with JSON serialization, among other things.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Read a file](#0-read-a-file)
  - [1. Write to a file](#1-write-to-a-file)
  - [2. Append to a file](#2-append-to-a-file)
  - [3. JSON serialization](#3-json-serialization)
  - [4. JSON deserialization](#4-json-deserialization)
  - [5. Save to a JSON file](#5-save-to-a-json-file)
  - [6. Load from a JSON file](#6-load-from-a-json-file)
  - [7. Add arguments to a list and save in JSON file](#7-add-arguments-to-a-list-and-save-in-json-file)
  - [8. Class to JSON](#8-class-to-json)
  - [9. Pascal's triangle](#9-pascals-triangle)
  - [10. Insert a string in a file](#10-insert-a-string-in-a-file)
  - [11. Compute metrics from stdin](#11-compute-metrics-from-stdin)
  
## Overview
The tasks in this project revolve around file input/output (I/O) operations in Python. Some highlights:
- Reading and writing files using the `with` statement.
- JSON serialization and deserialization using `json.dumps()` and `json.loads()`.
- Implementing Pascal's triangle.
- Working with logs and computing statistics from stdin inputs.

## Requirements
- Python 3.x
- Pycodestyle (for code linting)

## Tasks

### 0. Read a file
Write a function that reads a text file and prints it to stdout.
- Function: `def read_file(filename="")`
- Example:
    ```python
    read_file("my_file.txt")
    ```

### 1. Write to a file
Write a function that writes a string to a text file and returns the number of characters written.
- Function: `def write_file(filename="", text="")`

### 2. Append to a file
Write a function that appends a string to the end of a text file.
- Function: `def append_write(filename="", text="")`

### 3. JSON serialization
Write a function that returns the JSON representation of an object.
- Function: `def to_json_string(my_obj)`

### 4. JSON deserialization
Write a function that returns an object from a JSON string.
- Function: `def from_json_string(my_str)`

### 5. Save to a JSON file
Write a function that saves a Python object to a JSON file.
- Function: `def save_to_json_file(my_obj, filename)`

### 6. Load from a JSON file
Write a function that creates an object from a JSON file.
- Function: `def load_from_json_file(filename)`

### 7. Add arguments to a list and save in JSON file
Write a script that adds all arguments to a Python list and saves them in a file as JSON.
- Script: `7-add_item.py`

### 8. Class to JSON
Write a class `Student` that defines a student by:
- Attributes: `first_name`, `last_name`, `age`
- Method: `to_json(self)` returns the dictionary representation of the instance.

### 9. Pascal's triangle
Write a function that returns a list of lists representing Pascal’s triangle of `n`.
- Function: `def pascal_triangle(n)`

### 10. Insert a string in a file
Write a function that inserts a line of text after each line containing a specific string.
- Function: `def append_after(filename="", search_string="", new_string="")`

### 11. Compute metrics from stdin
Write a script that reads from stdin and computes metrics (such as total file size and number of status codes).
- Script: `101-stats.py`

## Fun Fact
Did you know that Pascal's triangle was used in China centuries before Pascal popularized it in Europe? It's sometimes referred to as the Yang Hui triangle in China.
