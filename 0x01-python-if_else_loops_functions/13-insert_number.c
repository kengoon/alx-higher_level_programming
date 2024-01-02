#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_list = *head;
	listint_t *temp_var = NULL;
	listint_t *new_list = NULL;

	new_list = malloc(sizeof(listint_t));
	if (!new_list)
		return (NULL);

	new_list->n = number;
	new_list->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}
	else
	{
		while (current_list && current_list->n < number)
		{
			temp_var = current_list;
			current_list = current_list->next;
		}
		temp_var->next = new_list;
		new_list->next = current_list;
	}
	return (new_list);
}
