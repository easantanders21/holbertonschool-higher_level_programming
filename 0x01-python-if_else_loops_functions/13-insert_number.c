#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node
 * @head: Linked list
 * @number: number
 *
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2, *newn;

	newn = malloc(sizeof(listint_t));
	if (!newn)
		return (NULL);
	newn->n = number;
	temp = NULL;
	temp2 = *head;

	while (temp2 && temp2->n < number)
	{
		temp = temp2;
		temp2 = temp2->next;
	}

	newn->next = temp2;
	if (temp)
		temp->next = newn;
	else
		*head = newn;
	return (temp2);
}
