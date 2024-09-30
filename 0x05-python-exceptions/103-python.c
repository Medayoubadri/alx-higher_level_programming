#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			print_python_float(item);
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t print_size = size > 10 ? 10 : size;
	char *string = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", print_size);

	for (Py_ssize_t i = 0; i < print_size; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("  value: %g\n", value);
}

