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
	listint_t *temp, *temp2, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	temp = NULL;
	temp2 = *head;

	while (temp2->n < number && temp2)
	{
		temp = temp2;
		temp2 = temp2->next;
	}

	new->next = temp2;
	if (temp)
		temp->next = new;
	else
		*head = new;
	return (temp2);
}
