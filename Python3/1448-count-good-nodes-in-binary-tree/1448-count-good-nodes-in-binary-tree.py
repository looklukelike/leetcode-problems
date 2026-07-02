# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    n: int
    def goodNodes(self, root: TreeNode) -> int:
        self.n = 0
        def count(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.n += 1

            max_val = max(node.val, max_val)

            count(node.left, max_val)
            count(node.right, max_val)  
        
        count(root, root.val)
        return self.n
        