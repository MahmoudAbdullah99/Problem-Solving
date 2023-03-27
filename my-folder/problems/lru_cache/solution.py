class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left_pointer = Node(0,0)
        self.right_pointer = Node(0,0)

        self.left_pointer.next = self.right_pointer
        self.right_pointer.prev = self.left_pointer



    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node):
        prev_node = self.right_pointer.prev
        
        prev_node.next = self.right_pointer.prev = node
        node.next = self.right_pointer
        node.prev = prev_node


    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node:
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1


    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left_pointer.next
            self.remove(lru)
            self.cache.pop(lru.key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)