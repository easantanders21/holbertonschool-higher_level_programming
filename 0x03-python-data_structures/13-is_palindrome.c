#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - return palindrome
 * @head: double pointor to list
 * Return: palindrome 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *count = *head, *rec = *head;
	int i = 0, j = 0, *array = NULL, k = 0;

	if (head == NULL)
		return (1);
	while (count)
	{
		count = count->next;
		i++;
	}
	array = malloc(sizeof(int) * i);
	while (rec)
	{
		array[j] = rec->n;
		rec = rec->next;
		j++;
	}
	while (k <= i / 2)
	{
		if (array[k] != array[i - 1 - k])
			return (0);
		k++;
	}
	return (1);
}
