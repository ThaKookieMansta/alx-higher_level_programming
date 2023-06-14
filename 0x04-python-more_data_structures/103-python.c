#include <Python.h>

void print_python_list(PyObject *p);


/**
 * print_python_bytes - Prints info on Python byte objects
 * @p: A byte object.
 */
void print_python_bytes(PyObject *p)
{
  unsigned char n, size;
  PyBytesObject *bytes = (PyBytesObject *)p;

  printf("[.] bytes object info\n");
  if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
  printf("  trying string: %s\n", bytes->ob_sval);

  if (((PyVarObject *)p)->ob_size > 10)
    size = 10;
  else
    size = ((PyVarObject *)p)->ob_size + 1;

  printf("  first %d bytes: ", size);
  for (n = 0; n < size; n++)
    {
      printf("%02hhx", bytes->ob_sval[n]);
      if (n == (size - 1))
	printf("\n");
      else
	printf(" ");
    }
}

/**
 * print_python_list - Prints info Python lists.
 * @p: A PyObject object for lists
 */
void print_python_list(PyObject *p)
{
  int size, alloc, n;
  const char *type;
  PyListObject *list = (PyListObject *)p;
  PyVarObject *var = (PyVarObject *)p;

  size = var->ob_size;
  alloc = list->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", alloc);

  for (n = 0; n < size; n++)
    {
      type = list->ob_item[n]->ob_type->tp_name;
      printf("Element %d: %s\n", n, type);
      if (strcmp(type, "bytes") == 0)
	print_python_bytes(list->ob_item[n]);
    }
}

