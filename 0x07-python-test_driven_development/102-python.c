#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	fflush(stdout);

	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	printf("[.] string object info\n");
	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *string_value = PyUnicode_AsUTF8(p);

	if (PyUnicode_IS_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	printf("  length: %ld\n", length);
	printf("  value: %s\n", string_value);
}
