# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def descend(node):
            if not node:
                return []
            
            if node.val == val:
                return [node]
            
            return descend(node.left) + descend(node.right)

        solution = descend(root)
        return None if len(solution) == 0 else solution[0]