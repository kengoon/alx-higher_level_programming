#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;

	if (!s)
		return (0);

	while (s && s->next)
	{
		s = s->next;
		if (s == list)
			return (1);
	}
	return (0);
}
