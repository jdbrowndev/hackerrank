"""
Author: Jordan Brown
Date: 8-6-16

Deletes duplicate values from a sorted linked list.

Link to problem: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list
"""
def RemoveDuplicates(head):
    if head is not None and head.next is not None:
        prev = head
        current = head.next
        while current is not None:
            if prev.data == current.data:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
    return head