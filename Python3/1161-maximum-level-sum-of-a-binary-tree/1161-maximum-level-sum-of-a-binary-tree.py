# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = dict()

        def descend(node, depth):
            if node is None:
                return 
            
            if depth not in d:
                d[depth] = 0
            d[depth] += node.val

            if node.left:
                descend(node.left, depth + 1)

            if node.right:
                descend(node.right, depth + 1)

        descend(root, 0)

        l = list(d.values())
        max_value = float('-inf')
        idx = None
        for i, val in enumerate(l):
            if val > max_value:
                max_value = val
                idx = i + 1
        
        return idx