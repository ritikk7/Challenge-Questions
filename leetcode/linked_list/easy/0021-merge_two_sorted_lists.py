# Problem: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy
# Time complexity: O(n + m)
# Space complexity: O(1)

# Solution: Use a dummy node to simplify list merging. Iterate through both lists, appending the smaller node to the merged list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        
        return head.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    print("Test Case 1:")
    print_linked_list(solution.mergeTwoLists(l1, l2))  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    # Test Case 2
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    print("Test Case 2:")
    print_linked_list(solution.mergeTwoLists(l1, l2))  # Output: (empty)

    # Test Case 3
    l1 = create_linked_list([])
    l2 = create_linked_list([0])
    print("Test Case 3:")
    print_linked_list(solution.mergeTwoLists(l1, l2))  # Output: 0

if __name__ == "__main__":
    main()
