"""
Author: Jordan Brown
Date: 8-6-16

Reverses a doubly linked list.

Link to problem: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list
"""
def Reverse(head):
    if head is None or head.next is None:
        return head
    prev = head
    current = head.next
    head.prev = head.next
    head.next = None
    while current is not None:
        oldNext = current.next
        current.next = prev
        current.prev = oldNext
        prev = current
        current = oldNext
    return prev