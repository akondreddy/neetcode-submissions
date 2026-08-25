# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node):
            # If it isn't a node, simply return
            # without doing anything
            if node == None:
                return
            # Swap left and right nodes
            temp = node.left
            node.left = node.right
            node.right = temp
            # Recursively iterate through the 
            # binary tree
            recurse(node.left)
            recurse(node.right)
        # Perform operation starting from root    
        recurse(root)
        # Return the binary tree
        return root