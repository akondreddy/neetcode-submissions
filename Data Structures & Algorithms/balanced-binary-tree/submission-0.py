# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node):
            # Reach the end of a subtree
            if not node:
                return 0, True
            # Computes heights
            leftHeight, leftBalanced = recurse(node.left)
            rightHeight, rightBalanced = recurse(node.right)

            # Returns the max height of the subtree
            maxHeight = 1 + max(leftHeight, rightHeight)

            # Calculates difference for height-balanced
            difference = abs(leftHeight - rightHeight)
            
            balanced = leftBalanced and rightBalanced and difference <= 1

            # Give parent height information
            return maxHeight, balanced

        rootHeight, rootBalanced = recurse(root)

        return rootBalanced
        