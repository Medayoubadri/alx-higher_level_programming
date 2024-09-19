#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject pointer to a Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("\t[ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = list->ob_size;
	allocated = list->allocated;

	printf("\tSize of the Python List = %zd\n", size);
	printf("\tAllocated = %zd\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];

		printf("\tElement %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, x;
	PyBytesObject *bytes_obj;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("\t[ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes_obj = (PyBytesObject *)p;
	size = bytes_obj->ob_size;
	string = bytes_obj->ob_sval;

	printf("\tsize: %ld\n", size);
	printf("\ttrying string: %s\n", string);
	if (size + 1 < 10)
		x = size + 1;
	else
		x = 10;
	printf("\tfirst %ld bytes:", x);
	for (i = 0; i < x; i++)
	{
		printf(" %02hhx", string[i]);
	}
	printf("\n");
}
