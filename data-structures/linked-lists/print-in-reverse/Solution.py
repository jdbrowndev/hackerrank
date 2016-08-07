"""
Author: Jordan Brown
Date: 8-6-16

Prints a linked list in reverse order.

Link to problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse
"""
def ReversePrint(head):
    output = ""
    current = head
    while current != None:
        output = str(current.data) + ("" if current == head else "\n") + output
        current = current.next
    if len(output) > 0: print(output)