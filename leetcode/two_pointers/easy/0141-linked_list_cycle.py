# Problem: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Time complexity: O(n), where n is the number of nodes in the list
# Space complexity: O(1), using Floyd's Tortoise and Hare algorithm (two pointers)

# Solution: Use two pointers (slow and fast). Move slow by 1 step and fast by 2 steps.
# If there's a cycle, they will eventually meet. If fast reaches the end, there's no cycle.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

# Test cases
def main():
    solution = Solution()

    # Helper to create a linked list with optional cycle
    def create_linked_list(values, pos):
        if not values:
            return None
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    # Test Case 1: cycle exists
    head = create_linked_list([3, 2, 0, -4], 1)
    print("Test Case 1:", solution.hasCycle(head))  # Output: True

    # Test Case 2: cycle exists
    head = create_linked_list([1, 2], 0)
    print("Test Case 2:", solution.hasCycle(head))  # Output: True

    # Test Case 3: no cycle
    head = create_linked_list([1], -1)
    print("Test Case 3:", solution.hasCycle(head))  # Output: False

    # Test Case 4: no cycle
    head = create_linked_list([1, 2, 3], -1)
    print("Test Case 4:", solution.hasCycle(head))  # Output: False

if __name__ == "__main__":
    main()
