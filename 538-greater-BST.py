# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    def convertHelper(self, root):
        if(root == None):
            return 0
        else:
            get_val = self.convertHelper(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertHelper(root.left)            
            
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root == None):
            return root
        self.convertHelper(root)
        return root
