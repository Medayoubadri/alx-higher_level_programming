#!/usr/bin/python3
def safe_print_integer(value):
	"""
	Attempts to print the value as an integer.
	Just trying to fit non-integers into '{:d}'.
	"""
	try:
		print("{:d}".format(value))
		return True
	except (ValueError, TypeError):
		# We accept our failure gracefully, like when you pretend you meant to trip over your own feet.
		return False
