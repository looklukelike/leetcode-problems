# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0
        if root.left == root.right and root.right == None:
            return self.max_depth

        def descend(node, gone_left, depth):
            if not node:
                return None
            
            self.max_depth = max(self.max_depth, depth)

            if node.left:
                zigzag = gone_left == False or node == root
                if zigzag:
                    descend(node.left, True, depth + 1)
                else:
                    descend(node.left, True, 1)
            if node.right:
                zigzag = gone_left == True or node == root
                if zigzag:
                    descend(node.right, False, depth + 1)
                else:
                    descend(node.right, False, 1)
        
        descend(root, False, 0)

        return self.max_depth
