#include "Python.h"

/**
 * print_python_string - Prints Python strings.
 * @p: The string.
 */
void print_python_string(PyObject *p)
{
	long int string_length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	string_length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", string_length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &string_length));
}
