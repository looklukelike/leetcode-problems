# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaves(self, node: TreeNode):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self.get_leaves(node.left) + self.get_leaves(node.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)
        