# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def MergeTrees(t1, t2):
            
            if (not t1):
                return t2
            if (not t2):
                return t1
            t1.val += t2.val
            t1.left = MergeTrees(t1.left, t2.left)
            t1.right = MergeTrees(t1.right, t2.right)
            return t1
        
        return MergeTrees(root1, root2)
        