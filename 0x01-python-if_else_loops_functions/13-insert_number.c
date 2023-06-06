#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

listint_t *create_node(int n);

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the linked list
 * @number: the new data
 * Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *this_node = NULL, *new_node = NULL;

	if (!head)
	{
		return (NULL);
	}
	else if (!(*head))
	{
		new_node = create_node(number);
		*head = new_node;
		return (new_node);
	}

	this_node = *head;
	while (this_node)
	{
		if (this_node->n >= number)
		{
			new_node = create_node(number);
			new_node->next = this_node;
			*head = new_node;
			return (new_node);
		}
		else if (this_node->n <= number)
		{
			if (!this_node->next || this_node->next->n >= number)
			{
				new_node = create_node(number);
				new_node->next = this_node->next;
				this_node->next = new_node;
				return (this_node->next);
			}
		}
		this_node = this_node->next;
	}
	return (NULL);

}

/**
 * create_node - Creates nodes for the linked lists
 * @n: The node data
 * Return:PTR to the new node
*/
listint_t *create_node(int n)
{
	listint_t *r = NULL;

	r = malloc(sizeof(listint_t));
	if (!r)
		return (NULL)
	r->next = NULL;
	r->n = n;
}
