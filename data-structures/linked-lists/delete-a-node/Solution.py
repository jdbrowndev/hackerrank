"""
Author: Jordan Brown
Date: 8-6-16

Deletes a node at a specific position in a linked list.

Link to problem: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
"""
def Delete(head, position):
    if position == 0:
        return head.next
    else:
        prev = current = head
        for i in range(1, position + 1):
            prev = current
            current = current.next
        prev.next = current.next
        return head