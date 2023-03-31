# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        
        if root:
            q.append((root, depth))

        while q:
            node, depth = q.popleft()

            if node:
                q.extend([(node.left, depth+1), (node.right, depth+1)])
                    
        return depth

