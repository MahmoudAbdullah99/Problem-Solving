# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB:
            currA, currB = headA, headB
            len_listA, len_listB = 0, 0

            while currA:
                len_listA +=1
                currA = currA.next
            
            while currB:
                len_listB +=1
                currB = currB.next
            
            currA, currB = headA, headB
            diff = abs(len_listA - len_listB)
            # print(len_listA, len_listB, diff)
            
            if len_listA > len_listB:
                for i in range(diff):
                    currA = currA.next
                    # print("currA.val ", currA.val)
            elif len_listA < len_listB:
                for i in range(diff):
                    currB = currB.next
                    # print("currB.val ", currB.val)
            
            while currA != currB:
                    currA, currB = currA.next, currB.next

            return currA
        
        return 