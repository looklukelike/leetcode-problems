class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(node, _min, _max):
            if node is None:
                return True
            
            isValid = node.val > _min and node.val < _max
            if not isValid:
                return False

            if node.left:
                if node.left.val < node.val:
                    isValid = isValid and recurse(node.left, _min, node.val)
                else:
                    isValid = False

            if node.right:
                if node.right.val > node.val:
                    isValid = isValid and recurse(node.right, node.val, _max)
                else:
                    isValid =  False
        
            return isValid

        return recurse(root, float('-inf'), float('+inf'))
