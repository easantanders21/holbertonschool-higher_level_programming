#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Print Python List
 * @p: list from python
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int Py_ssize_t = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %i\n", Py_ssize_t);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < Py_ssize_t; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
