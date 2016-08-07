"""
Author: Jordan Brown
Date: 8-6-16

Prints all elements of a linked list.

Link to problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list
"""
def print_list(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next