"""
Author: Jordan Brown
Date: 8-6-16

Inserts a node at the end of a linked list.

Link to problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
"""
def Insert(head, data):
    if head == None:
        head = Node(data)
    else:
        tail = head
        while tail.next != None:
            tail = tail.next
        tail.next = Node(data)
    return head