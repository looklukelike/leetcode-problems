# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        if not root.left:
            return root.right

        if not root.right:
            return root.left

        next_node = root.right
        while next_node.left:
            next_node = next_node.left
        
        next_node.left = root.left

        root = root.right

        return root
