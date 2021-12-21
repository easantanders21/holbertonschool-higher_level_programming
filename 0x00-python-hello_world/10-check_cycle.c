#include "lists.h"
/**
 * check_cycle - return 1 if list is a cycle
 * @list: Linked list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	if (list == NULL)
		return (0);

	while (temp2->next != NULL)
	{
		temp = temp->next;
		temp2 = temp2->next;
		if (temp2->next == NULL)
			break;
		temp2 = temp2->next;
		if (temp2 == temp)
			return (1);
	}

	return (0);
}
