# Problem: Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Time complexity: O(n), where n is the number of nodes in the list
# Space complexity: O(1), using two-pointer technique

# Solution: Use two pointers (slow and fast). Move slow by 1 and fast by 2 steps.
# When fast reaches the end, slow will be at the middle node.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Test cases
def main():
    solution = Solution()

    # Helper to create linked list and return head
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Helper to convert linked list to list (for output)
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Test Case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = solution.middleNode(head)
    print("Test Case 1:", linked_list_to_list(middle))  # Output: [3, 4, 5]

    # Test Case 2
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    middle = solution.middleNode(head)
    print("Test Case 2:", linked_list_to_list(middle))  # Output: [4, 5, 6]

    # Test Case 3
    head = create_linked_list([1])
    middle = solution.middleNode(head)
    print("Test Case 3:", linked_list_to_list(middle))  # Output: [1]

if __name__ == "__main__":
    main()
