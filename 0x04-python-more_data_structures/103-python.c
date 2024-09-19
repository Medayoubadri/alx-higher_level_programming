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
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	allocated = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_CheckExact(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	if (size < 10)
		limit = size + 1;
	else
		limit = 10;

	printf("  first %zd bytes:", limit);
	for (i = 0; i < limit; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}
