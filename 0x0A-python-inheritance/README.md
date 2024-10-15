# 0x0A. Python - Inheritance

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## Tasks
### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.
- Prototype: `def lookup(obj):`
- Returns a list object
- You are not allowed to import any module

### 1. My list
Write a class `MyList` that inherits from `list`:
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- You are not allowed to import any module

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
- Prototype: `def is_same_class(obj, a_class):`
- You are not allowed to import any module

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
- Prototype: `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

### 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
- Prototype: `def inherits_from(obj, a_class):`
- You are not allowed to import any module

### 5. Geometry module
Write an empty class `BaseGeometry`.
- You are not allowed to import any module

### 6. Improve Geometry
Write a class `BaseGeometry` (based on `5-base_geometry.py`).
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- You are not allowed to import any module

### 7. Integer validator
Write a class `BaseGeometry` (based on `6-base_geometry.py`).
- Public instance method: `def integer_validator(self, name, value):` that validates value:
  - you can assume `name` is always a string
  - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are not allowed to import any module

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py):
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- You must validate `width` and `height` by using `integer_validator` (see `7-base_geometry.py`)
- You are not allowed to import any module

### 9. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py). (task based on `8-rectangle.py`)
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- Print the rectangle in the following format: `[Rectangle] <width>/<height>`
- You are not allowed to import any module

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py):
- Instantiation with `size`: `def __init__(self, size):`
- You must validate `size` by using `integer_validator`
- The `__init__` method of the `Square` should call the `__init__` method of `Rectangle` with `width` and `height` as `size`
- You are not allowed to import any module

### 11. Square #2
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (task based on `10-square.py`)
- Print the square in the following format: `[Square] <size>/<size>`
- You are not allowed to import any module

### Advanced Tasks
### 12. My integer
Write a class `MyInt` that inherits from `int`:
- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
- You are not allowed to import any module

### 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:
- Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
- You are not allowed to use `try/except`
- You are not allowed to import any module


# Fun Fact:
Bananas are radioactive! 🍌 Bananas contain potassium-40, a radioactive isotope of potassium. But don't worry—you'd have to eat over 10 million bananas in one sitting for it to have any harmful effects. So, keep enjoying your healthy snack without fear of turning green!
