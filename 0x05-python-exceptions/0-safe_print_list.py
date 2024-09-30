#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	"""
	Prints 'x' elements from my_list.
	
	It's like playing Jenga with the list: just hope nothing goes out of bounds.
	"""
	num_printed = 0
	for i in range(x):
		try:
			print(my_list[i], end="")
			num_printed += 1
		except IndexError:
			# If we go out of bounds, let's stop without making a fuss.
			break
	print()
	return num_printed
