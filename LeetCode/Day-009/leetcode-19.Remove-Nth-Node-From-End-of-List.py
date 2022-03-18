"""
Problem Description:
    - Given the head of a linked list, remove the nth node from the end of the
    list and return its head.

Notes:
    - 
    - 

TODO:
    - Add notes
    - Review
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEndRecursive(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def remove(head, n):
            if head == None:
                return head, 0
            
            head.next, counter = remove(head.next, n)
            counter += 1
               
            if counter == n:
                head = head.next
            
            return head, counter
        
        return remove(head, n)[0]
    def removeNthFromEndIterative(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer = ListNode(-1, head)
        len_list = 0

        while head:
            head = head.next
            len_list += 1
        
        node_n = len_list-n
        head = pointer.next

        if node_n == 0:
            return head.next
        
        while node_n > 0:
            pointer = pointer.next
            node_n -= 1
        
        pointer.next = pointer.next.next

        return head
