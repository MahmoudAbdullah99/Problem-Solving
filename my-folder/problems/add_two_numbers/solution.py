# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp = ListNode(-1)
        head = temp

        while l1 or l2 or carry:
            n1, n2 = 0, 0

            if l1:
                n1 = l1.val 
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next


            sum_ = n1 + n2 + carry
            curr = sum_ % 10
            carry = sum_ // 10

            temp.next = ListNode(curr)
            temp = temp.next
        
        return head.next
            


