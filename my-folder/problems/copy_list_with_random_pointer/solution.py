"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        org_copy = {}
        
        while temp:
            copy = Node(temp.val)
            org_copy[temp] = copy
            temp = temp.next
        
        temp = head
        
        while temp:
            copy = org_copy.get(temp)
            copy.next = org_copy.get(temp.next)
            copy.random = org_copy.get(temp.random)
            
            temp = temp.next
        
        return org_copy.get(head)