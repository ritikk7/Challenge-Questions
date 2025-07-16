# Problem: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Time complexity: O(n), where n is the number of nodes in the linked list
# Space complexity: O(1), in-place reversal using pointers

# Solution: Use three pointers to reverse the linked list iteratively:
# - `prv` tracks the previous node,
# - `cur` is the current node,
# - `nex` is the next node to process.
# After reversal, return the new head (last processed node).

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prv = None
        cur = head
        nex = cur.next

        while cur.next:
            cur.next = prv
            prv = cur
            cur = nex
            nex = nex.next

        cur.next = prv
        return cur

# Test cases
def main():
    solution = Solution()

    # Helper to create linked list from list
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Helper to convert linked list to list
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Test Case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverseList(head)
    print("Test Case 1:", linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

    # Test Case 2
    head = create_linked_list([1, 2])
    reversed_head = solution.reverseList(head)
    print("Test Case 2:", linked_list_to_list(reversed_head))  # Output: [2, 1]

    # Test Case 3
    head = create_linked_list([1])
    reversed_head = solution.reverseList(head)
    print("Test Case 3:", linked_list_to_list(reversed_head))  # Output: [1]

    # Test Case 4
    head = create_linked_list([])
    reversed_head = solution.reverseList(head)
    print("Test Case 4:", linked_list_to_list(reversed_head))  # Output: []

if __name__ == "__main__":
    main()
