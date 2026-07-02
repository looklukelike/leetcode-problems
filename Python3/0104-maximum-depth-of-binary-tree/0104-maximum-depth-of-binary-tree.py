# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node, depth):
        if not node: return depth
        depth += 1
        return max(self.recurse(node.left, depth), self.recurse(node.right, depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:     
        return self.recurse(root, 0)    
        