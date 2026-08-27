# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # Checks where to look for if the subtree and tree
    # have overlap
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        
        # If there is overlap from the start
        if self.recurse(root, subRoot):
            return True
        
        # Otherwise, check the entire tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # Recursive method that defines do the 
    # tree and subtree match
    def recurse(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        # This is what checks the full subtree
        if root and subRoot and root.val == subRoot.val:
            return self.recurse(root.left, subRoot.left) and self.recurse(root.right, subRoot.right)
        return False


            