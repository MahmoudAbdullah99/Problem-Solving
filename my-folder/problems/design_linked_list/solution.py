class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is
        invalid, return -1.
        """
        if index < 0 or index >= self.size or not self.head:
            return -1

        cur_node = self.head

        for i in range(index):
            cur_node = cur_node.next

        return cur_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur_node = self.head

        if not cur_node:
            self.head = Node(val)
        else:
            while cur_node.next:
                cur_node = cur_node.next

            cur_node.next = Node(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended
        to the end of linked list. If index is greater than the length, the node
        will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
            return
        else:
            cur_node = self.head
            # Stopping before the index before which the new node will be
            # inserted
            for i in range(index - 1):
                cur_node = cur_node.next
            new_node = Node(val)
            new_node.next = cur_node.next
            cur_node.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        
        cur_node = self.head
        
        if index == 0:
            self.head = cur_node.next
        else:
            for i in range(index - 1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next

        self.size -= 1
