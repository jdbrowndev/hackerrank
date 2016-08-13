"""
Author: Jordan Brown
Date: 8-6-16

Detects a cycle within a linked list.

Link to problem: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
"""
def has_cycle(head):
    visited = set()
    current = head
    while current is not None:
        if current.data in visited:
            return True
        else:
            visited.add(current.data)
            current = current.next
    return False