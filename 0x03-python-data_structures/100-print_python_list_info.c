#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about
 * Python lists
 * @p: The pointer to generic PyObject
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	size_t my_length = 0, i = 0;
	const char *py_type = NULL;

	my_length = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", my_length);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	for  (; i < my_length; i++)
	{
		py_type = Py_TYPE(py_list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, py_type);
	}
}