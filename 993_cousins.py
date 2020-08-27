# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

    Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

    We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

    Return true if and only if the nodes corresponding to the values x and y are cousins.
        """
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents = {}
        depth = {}
        def helper(node, d = 0, parent = None):
            if node:
                parents[node.val] = parent if parent else None
                depth[node.val] = d
                helper(node.left, d + 1, node)
                helper(node.right, d + 1, node)
        helper(root)
        return parents[x] != parents[y] and depth[x] == depth[y]