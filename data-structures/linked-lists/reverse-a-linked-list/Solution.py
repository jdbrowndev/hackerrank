"""
Author: Jordan Brown
Date: 8-6-16

Reverses a linked list.

Link to problem: https://www.hackerrank.com/challenges/reverse-a-linked-list
"""
def Reverse(head):
    if head is None or head.next is None:
        return head
    else:
        prev = head
        current = head.next
        head.next = None
        while current is not None:
            oldNext = current.next
            current.next = prev
            prev = current
            current = oldNext
        return prev