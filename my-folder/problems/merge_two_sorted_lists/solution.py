# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            full_list = ListNode()
            temp = full_list
            
            while list1 and list2:
                if list1.val <= list2.val:
                    full_list.next = list1
                    list1 = list1.next
                else:
                    full_list.next = list2
                    list2 = list2.next
                
                full_list = full_list.next
            
            while list1 :
                full_list.next = list1
                list1 = list1.next
                full_list = full_list.next

            while list2:
                full_list.next = list2
                list2 = list2.next
                full_list = full_list.next

            return temp.next