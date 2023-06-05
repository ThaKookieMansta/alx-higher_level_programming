#include "lists.h"

/**
 * check_cycle - Checks if linked list is circular or not
 * @list: The linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *ll1 = NULL, *ll2 = NULL;

	ll1 = ll2 = list;

	while (list && ll1 && ll2 && ll1->next && ll2->next)
	{
		ll1 = ll1->next;
		ll2 = ll2->next->next;
		if (!ll2 || !ll1)
		{
			return (0);
		}

		if (ll2->next == ll1)
		{
			return (1);
		}
	}
	return(0);
}
