# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        # Returns the height
        def recurse(node):
            # nonlocal allows for the outer maxDiameter
            # variable to be recognized by the 
            # nested function. Without it, Python
            # assumes maxDiameter is a local var
            nonlocal maxDiameter
            if not node:
                return 0
            # Finds the height of left and right
            # subtrees
            leftHeight = recurse(node.left)
            rightHeight = recurse(node.right)

            # Updates the diameter 
            maxDiameter = max(maxDiameter, leftHeight + rightHeight)

            # Finds the height
            return 1 + max(leftHeight, rightHeight)
        
        recurse(root)
        return maxDiameter