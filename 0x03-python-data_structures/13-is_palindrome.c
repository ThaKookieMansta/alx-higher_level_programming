#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
  * is_palindrome - A function that checks if a singly linked 
  * list is a palindrome
  * @head: A double pointer to the head of the list.
  * Return: 0 if the list not a palindrome, 1 if it is.
  */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int nodes = 0, a = 0, *my_list = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		nodes++;
		temp = temp->next;
	}
	my_list = malloc(sizeof(int) * nodes);
	temp = *head;
	while (temp)
	{
		my_list[a++] = temp->n;
		temp = temp->next;
	}
	for (a = 0; a < nodes / 2; a++)
	{
		if (my_list[a] != my_list[nodes - 1 - a])
		{
			free(my_list);
			return (0);
		}
	}
	free(my_list);
	return (1);
}
