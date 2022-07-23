##### NOTES #####
#
#     h = height of perfect tree.
#     q = list of positive integers representing flux converters.
#         returns list of integers 
#         p = each element is a label that sits on top of the 
#         respective converter in q or -1 if no suh converter.
#       
# for example: solution (3, [1, 4, 7]} 
#         3 = height
#         returns [3, 6, -1].
#         because those are on top.
#       
#     1 <= h <= 30
#     h=1 = perfect binary tree with only the root.
#     h=2 = perfect binary tree with the root and two leaf nodes.
#     h=3 = perfect bonary tree with the root, two internal nodes and four
#         lead nodes. (example below)
#       
# for example:   7
#              3   6
#             1 2 4 5 
#
# lists q and p range from 1-1000 (1-2^h-1).
# 
# post order traversal

def find_parent(node, root, size):
    # Traverse the branch to find the parent node.

    if node < 1 or node >= root:
        return -1
    
    right = (root-1)
    left = (right-size)

    if node in (left, right):
        return root

    branch = left if node < left else right

    return find_parent(node, branch, size >> 1)

def solution(h, q):

    # Error handling.
    if (h < 1 or h > 30):
        raise ValueError('The input value is out of bounds')
    if  (len(q) < 1 or len(q) > 10000):
        raise ValueError('The input value is out of bounds')

    root = (2**h-1)
    
    size =(root>>1)

    p = [find_parent(node, root, size) for node in q]

    return p