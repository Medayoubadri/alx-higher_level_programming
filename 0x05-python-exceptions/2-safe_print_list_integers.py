#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	"""
	Prints the first x integers from my_list.
	Imagine you're on a dating app for integers—only swiping right on the ones that make the cut.
	"""
	num_printed = 0
	for i in range(x):
		try:
			print("{:d}".format(my_list[i]), end="")
			num_printed += 1
		except (ValueError, TypeError):
			# Not an integer? Move along silently—no drama here.
			continue
		except IndexError:
			# If we go out of range, let's gracefully bow out.
			break
	print()
	return num_printed
