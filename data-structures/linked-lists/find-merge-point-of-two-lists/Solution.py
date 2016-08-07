"""
Author: Jordan Brown
Date: 8-6-16

Finds a node where two linked lists intersect.

Link to problem: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
"""
def FindMergeNode(headA, headB):
    aKeys = set()
    currentA = headA
    while currentA is not None:
        aKeys.add(currentA.data)
        currentA = currentA.next
        
    currentB = headB
    while currentB is not None:
        if currentB.data in aKeys:
            return currentB.data
        currentB = currentB.next

    return -1