"""
Author: Jordan Brown
Date: 4-3-21

Solves the preorder traversal problem.

Link to problem: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    if root is not None:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)