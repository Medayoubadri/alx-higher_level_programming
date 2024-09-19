#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject pointer to a Python list object.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject **items = ((PyListObject *)p)->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = items[i];
		const char *type = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, type);
	}
}
/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	char *bytes = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes);

	Py_ssize_t print_size = size < 10 ? size + 1 : 10;

	printf("  first %zd bytes: ", print_size);
	for (Py_ssize_t i = 0; i < print_size; i++)
	{
		printf("%02x", (unsigned char) bytes[i]);
		if (i < print_size - 1)
			printf(" ");
	}
	printf("\n");
}
