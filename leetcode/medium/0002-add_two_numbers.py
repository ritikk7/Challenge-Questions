# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium
# Time complexity: O(max(m, n))
# Space complexity: O(max(m, n))

# Solution: Iterate through both linked lists while maintaining a carry. Construct a new linked list by computing the sum digit-by-digit.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, digit = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

# Test cases
def list_to_linked(lst):
    """ Helper function to convert a list to a linked list """
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_to_list(node):
    """ Helper function to convert a linked list back to a list """
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def main():
    solution = Solution()
    
    # Test Case 1
    l1 = list_to_linked([2, 4, 3])
    l2 = list_to_linked([5, 6, 4])
    print("Test Case 1:", linked_to_list(solution.addTwoNumbers(l1, l2)))  # Output: [7, 0, 8]
    
    # Test Case 2
    l1 = list_to_linked([0])
    l2 = list_to_linked([0])
    print("Test Case 2:", linked_to_list(solution.addTwoNumbers(l1, l2)))  # Output: [0]
    
    # Test Case 3
    l1 = list_to_linked([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked([9, 9, 9, 9])
    print("Test Case 3:", linked_to_list(solution.addTwoNumbers(l1, l2)))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]

if __name__ == "__main__":
    main()
