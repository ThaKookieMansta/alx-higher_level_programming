#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

listint_t *create_nodes(int n);

/**
* insert_node - inserts a node sorted in a linked list of ints
* @head: double pointer to head of LL, needed for modification in edge
* cases
* @number: data for new node
* Return: pointer to newly created node, NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *this_node = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = create_nodes(number);
		*head = new_node;
		return (new_node);
	}
	this_node = *head;
	while (this_node)
	{
		/* need to insert at head */
		if (this_node->n >= number)
		{
			new_node = create_nodes(number);
			new_node->next = this_node;
			*head = new_node;
			return (new_node);
		}
		else if (this_node->n <= number)
		{
			if (!this_node->next || this_node->next->n >= number)
			{
				new_node = create_nodes(number);
				new_node->next = this_node->next;
				this_node->next = new_node;
				return (this_node->next);
			}
		}
		this_node = this_node->next;
	}
	return (NULL); /* failed */
}


/**
 * create_nodes - creates a new node for the LL
 * @n: data to insert into new node
 *
 * Return: pointer to newly allocated node
 */
listint_t *create_nodes(int n)
{
	listint_t *ret = NULL;

	ret = malloc(sizeof(listint_t));
	if (!ret)
		return (NULL);
	ret->next = NULL;
	ret->n = n;
	return (ret);
}
