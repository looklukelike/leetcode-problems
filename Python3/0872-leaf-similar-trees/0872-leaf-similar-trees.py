# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def descend(self, node: TreeNode, leaves: list):
        if not node.left and not node.right:
            leaves.append(node.val)
            return leaves
        new_leaves = []
        if node.left:
            new_leaves = self.descend(node.left, [])
        if node.right:
            new_leaves.extend(self.descend(node.right, []))
        leaves.extend(new_leaves)
        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left = self.descend(root1, [])
        right = self.descend(root2, [])

        return left == right
        