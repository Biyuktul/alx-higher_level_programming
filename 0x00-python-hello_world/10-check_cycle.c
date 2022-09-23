#include "lists.h"
#include <stdlib.h>
/**
 *check_cycle-checks the presence of cycle
 *@list: pointer to listint_t
 *Return: int
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
