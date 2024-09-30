#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	"""
	Divides elements of two lists element by element.
	This is like dividing loot among pirates—sometimes there isn't enough, sometimes it's not loot at all, and sometimes someone's trying to split by zero.
	"""
	result_list = []

	for i in range(list_length):
		try:
			a = my_list_1[i]
			b = my_list_2[i]
			result = a / b
		except TypeError:
			print("wrong type")
			result = 0
		except ZeroDivisionError:
			print("division by 0")
			result = 0
		except IndexError:
			print("out of range")
			result = 0
		finally:
			result_list.append(result)

	return result_list
