from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            q_size = len(queue)
            for i in range(q_size):
                curr_node = queue.popleft()
                if q_size != i+1:
                    curr_node.next = queue[0]
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                    
        return root