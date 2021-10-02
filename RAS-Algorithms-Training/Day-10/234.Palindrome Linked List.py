""""
Problem Description:
    Given the head of a singly linked list, return true if it is a palindrome.

Notes:
    - We can use a stack to store the first half of the linked list,
    then comparing the second half with the pop of the stack element by element.

TODO:
    - Review.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        fast = head
        stack = []

        while fast:
            if fast.next:
                stack.append(head.val)
                fast = fast.next
            head = head.next
            fast = fast.next

        while head:
            if stack.pop() != head.val:
                return False
            head = head.next

        return True

    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        fast = head
        stack = []

        while fast and fast.next:
            stack.append(head.val)
            head = head.next
            fast = fast.next.next

        if fast:
            head = head.next

        while head:
            if stack.pop() != head.val:
                return False
            head = head.next

        return True

    def isPalindrome_3(self, head: Optional[ListNode]) -> bool:
        prev = None
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        if fast:
            head = head.next

        while head:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next

        return not prev
