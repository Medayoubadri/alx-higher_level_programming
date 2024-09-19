#include <Python.h>
#include <stdio.h>


/**
* print_python_bytes - Prints details about a Python bytes object.
* @p: The Python object (should be of type bytes).
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_string;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &bytes_string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", bytes_string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

		for (i = 0; i < size + 1 && i < 10; i++)
		{
			printf(" %02hhx", bytes_string[i]);
		}
		printf("\n");
	}
}

/**
* print_python_list - Prints details about a Python list object.
* @p: The Python object (should be of type list).
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	PyObject *item;
	int i;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);

			if (PyBytes_Check(item))
				print_python_bytes(item);
		}
	}
	else
	{
		printf("[ERROR] Invalid List Object\n");
	}
}
