""""
Problem Description:
    Given the heads of two singly linked-lists headA and headB, return the
    node at which the two lists intersect. If the two linked lists have no
    intersection at all, return null.

Notes:
    - Approach 1:
    Using two pointers to the two heads of the two list, and by
    concatenating the two lists in opposite orders, A+B and B+A, we are sure
    that if there is an intersection, the two pointers will have the same
    value at some point. for example if the first list has 7 nodes and the
    second has 5 nodes, and their intersection is the last 3 nodes,
    by concatenating them the first pointer will walk (7+(5-3)) = 9 nodes and
    the second will walk (5+(7-3)) = 9 before the intersection which ensures
    hey will get to it in the same time.

    - Approach 2:
    As the same lists should at some point point to the same node, changing
    the values of one of the linked lists nodes values to a the negative
    same values instead will ensures if the second lists has a node point to
    a node of the first list (point of intersection), we will find it by
    iterating the second list and checking for a negative value.

TODO:
    - Review.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> \
            ListNode:
        """

        We line up the ends of the two lists by concatenating them in
        opposite orders, A+B and B+A. Then we just need to check if at some
        point the two merged lists are pointing to the same node.

        Args:
            headA: The first linked list.
            headB: The second linked list.

        Returns:
            currA: The Node of intersection if existed, if not return None

        """
        if headA and headB:
            currA, currB = headA, headB

            while currA != currB:
                currA = headB if currA is None else currA.next
                currB = headA if currB is None else currB.next

            return currA

        return

    def changeSign(self, head: ListNode):
        """

        Args:
            head: Head of the linked list

        Returns:
            The same linked list but with negative values of its nodes

        """
        while (head):
            head.val *= -1
            head = head.next

    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> \
            ListNode:
        """

        We check for a node with a negative value (The intersection with the
        first list which we change its nodes values for this purpose).

        Args:
            headA: The first linked list.
            headB: The second linked list.

        Returns:
            headB: The Node of intersection if existed, if not return None

        """
        self.changeSign(headA)

        while (headB):
            if headB.val < 0: break
            headB = headB.next

        self.changeSign(headA)
        return headB
