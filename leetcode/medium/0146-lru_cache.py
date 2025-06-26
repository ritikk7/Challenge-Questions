# Problem: LRU Cache
# Link: https://leetcode.com/problems/lru-cache/description/
# Difficulty: Medium
# Time complexity: O(1) for both get and put operations
# Space complexity: O(capacity)

# Solution: Use a hashmap for O(1) access and a doubly linked list to maintain LRU order.

class LRUCache:

    class Node:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def delNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del node
        self.size -= 1

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.size = 0
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        oldNode = self.cache[key]
        newNode = self.Node(key, oldNode.val)
        self.delNode(oldNode)
        self.addNode(newNode)
        self.cache[key] = newNode

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.delNode(oldNode)
        elif self.size == self.cap:
            oldNode = self.tail.prev
            del self.cache[oldNode.key]
            self.delNode(oldNode)

        newNode = self.Node(key, value)
        self.addNode(newNode)
        self.cache[key] = newNode

# Test cases
def main():
    # Test Case 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print("Test Case 1 - get(1):", lru.get(1))  # Output: 1
    lru.put(3, 3)  # evicts key 2
    print("Test Case 1 - get(2):", lru.get(2))  # Output: -1
    lru.put(4, 4)  # evicts key 1
    print("Test Case 1 - get(1):", lru.get(1))  # Output: -1
    print("Test Case 1 - get(3):", lru.get(3))  # Output: 3
    print("Test Case 1 - get(4):", lru.get(4))  # Output: 4

if __name__ == "__main__":
    main()
