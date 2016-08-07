"""
Author: Jordan Brown
Date: 8-6-16

Inserts a node into a sorted doubly linked list.

Link to problem: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
"""
def SortedInsert(head, data):
    if head is None:
        return Node(data)
    prev = current = head
    while current is not None and current.data < data:
        prev = current
        current = current.next
    node = Node(data, current, prev)
    prev.next = node
    if current is not None:
        current.prev = node
    return head