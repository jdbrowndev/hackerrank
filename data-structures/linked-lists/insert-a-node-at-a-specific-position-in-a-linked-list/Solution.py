"""
Author: Jordan Brown
Date: 8-6-16

Inserts a node at a specific position in a linked list.

Link to problem: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
"""
def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        prev = current = head
        for i in range(1, position + 1):
            prev = current
            current = current.next
        node = Node(data, current)
        prev.next = node
        return head