"""
Author: Jordan Brown
Date: 8-6-16

Merges two sorted linked lists.

Link to problem: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists
"""
def MergeLists(headA, headB):
    
    # Check for nulls.
    if headA is None:
        return headB
    if headB is None:
        return headA
    
    # Set currentA, currentB such that currentA's initial value is less than currentB's initial value.
    # currentA's list will eventually become the output linked list -- store the head in outputHead.
    currentA = outputHead = headA if headA.data < headB.data else headB
    currentB = headB if headA.data < headB.data else headA
    
    # Continue until there are no more values from currentB's list to merge into currentA.
    while currentB is not None:
        if currentB.data >= currentA.data and (currentA.next is None or currentB.data < currentA.next.data):
            oldANext = currentA.next
            oldBNext = currentB.next
            currentA.next = currentB
            currentB.next = oldANext
            currentA = currentB
            currentB = oldBNext
        else:
            currentA = currentA.next

    return outputHead;