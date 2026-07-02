# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = dict()

        def descend(node, depth):
            if not node:
                return None

            if depth not in values:
                values[depth] = node.val
            
            if node.right:
                descend(node.right, depth + 1)
            if node.left:
                descend(node.left, depth + 1)

        descend(root, 0)
        return list(values.values())