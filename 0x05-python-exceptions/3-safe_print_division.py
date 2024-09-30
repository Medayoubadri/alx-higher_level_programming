#!/usr/bin/python3
def safe_print_division(a, b):
	"""
	Divides two integers and prints the result.
	Dividing by zero is like trying to find common sense on the internet—it's just not going to happen.
	"""
	result = None
	try:
		result = a / b
	except ZeroDivisionError:
		# Caught trying to break the universe with a zero divisor. We say no.
		result = None
	finally:
		print("Inside result: {}".format(result))
	return result
