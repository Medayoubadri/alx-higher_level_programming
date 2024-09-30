#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
	"""
	Attempts to print value as an integer, catching errors and printing them to stderr.
	Trying to convince a non-integer that it's an integer.
	"""
	try:
		print("{:d}".format(value))
		return True
	except (ValueError, TypeError) as error:
		print("Exception: {}".format(error), file=sys.stderr)
		return False
