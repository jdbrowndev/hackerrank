"""
Author: Jordan Brown
Date: 8-6-16

Gets a node's value relative to the tail of a linked list.

Link to problem: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
"""
def GetNode(head, position):
    # Store last N elements seen where N = position + 1.
    # This way, when the end of the linked list is reached, we return the last element in the list.
    lastElementsSeen = []
    current = head
    while current is not None:
        if len(lastElementsSeen) == position + 1:
            del lastElementsSeen[-1]
        lastElementsSeen.insert(0, current)
        current = current.next
    return lastElementsSeen[-1].data