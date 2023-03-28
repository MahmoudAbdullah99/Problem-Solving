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
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return full_list.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        while len(lists) > 1:
            i = 0
            while i < len(lists):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                lists[i:i+2] = [self.mergeTwoLists(list1, list2)]
                i = i+1 
                    
        return lists[0]
































