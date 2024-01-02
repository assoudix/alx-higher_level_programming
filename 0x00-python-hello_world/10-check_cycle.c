#include "lists.h"

/**
 * check_cycle - implementation of Floyd's algorithm
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	if (!list)
		return (0);

	while (tort && hare && hare->next)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
		return (1);
	}

	return (0);
}


