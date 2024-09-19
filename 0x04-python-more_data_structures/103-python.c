#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject pointer to a Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("\t[ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = list->ob_size;
	allocated = list->allocated;

	printf("\tSize of the Python List = %ld\n", size);
	printf("\tAllocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];

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
	x = size < 10 ? size : 10;

	printf("\tfirst %ld bytes:", x);
	for (i = 0; i < x; i++)
	{
		printf(" %02hhx", string[i]);
	}
	printf("\n");
}
