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
	listint_t *temp = *head;
	listint_t *temp2 = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	temp2 = temp2->next;

	while (temp2->n < number && temp2)
	{
		temp = temp->next;
		temp2 = temp2->next;
		if (temp2->next == NULL)
		{
			temp2->next = new;
			new->next = NULL;
			return (new);
		}
	}

	new->next = temp2;
	temp->next = new;
	return (new);
}
