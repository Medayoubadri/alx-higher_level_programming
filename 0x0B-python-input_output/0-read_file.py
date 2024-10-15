#!/usr/bin/python3
"""
Reads a file and prints it—because printing is basically
just screaming at the screen.
"""


def read_file(filename=""):
	"""
	Reads a UTF8 text file and prints it to stdout.
	"""
	with open(filename, 'r', encoding='utf-8') as file:
		print(file.read(), end="")
