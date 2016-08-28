"""
Author: Jordan Brown
Date: 8-28-16

Solves the even tree problem via depth-first search.

Link to problem: https://www.hackerrank.com/challenges/even-tree
"""

def get_max_edges_removed_for_even_tree(tree):
    """
    Returns the maximum possible number of edges that can be removed from a tree to produce forests containing
    an even number of nodes.
    
    @param tree: Adjacency list representing the input tree.
    """
    
    # Shallow copy tree to prevent input from being modified.
    tree = tree.copy()
    # Use stack for depth-first search.
    stack = [1]
    
    edgesRemoved = 0
    while len(stack) > 0:
        current = stack.pop()
        if current in tree:
        
            # Shallow copy children to prevent the list from being modified while iterating.
            children = list(tree[current])
            
            for i in range(len(children)):
                if is_even_forest(children[i], tree):
                    tree[current].remove(children[i])
                    edgesRemoved += 1
            stack += children
    return edgesRemoved

def is_even_forest(node, tree):
    """
    Given a node in the tree, determines if the node and its subtree contain an even number of nodes.
    
    @param node: Node to begin count.
    @param tree: Adjacency list representing the entire tree.
    """
    
    count = 1
    if node in tree:
        children = tree[node]
        while len(children) > 0:
            count += len(children)
            nextChildren = []
            for i in range(len(children)):
                if children[i] in tree:
                    nextChildren += tree[children[i]]
            children = nextChildren
    return count % 2 == 0
    
(n, m) = (int(x) for x in input().split())

# Use adjacency list to represent the tree.
tree = {}

for _ in range(m):

     # u, v are reversed intentionally to start edges from parent to child.
    (v, u) = (int(x) for x in input().split())
    
    if u in tree:
        tree[u].append(v)
    else:
        tree[u] = [v]
print(get_max_edges_removed_for_even_tree(tree))