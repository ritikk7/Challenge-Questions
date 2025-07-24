# Problem: Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium
# Time complexity: O(H + k), where H is the height of the tree
# Space complexity: O(H) due to the recursion stack

# Solution: Perform an in-order traversal (left -> node -> right), which gives sorted order in BST.
# Decrement k as we visit nodes. When k == 0, we've found the kth smallest element.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.k = k

        def walk(node):
            if not node:
                return

            walk(node.left)

            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            walk(node.right)
        
        walk(root)
        return self.result

# Test cases
def main():
    solution = Solution()

    # Helper function to construct BST from list input (for testing)
    def insert_level_order(arr, i=0):
        if i >= len(arr) or arr[i] is None:
            return None
        root = TreeNode(arr[i])
        root.left = insert_level_order(arr, 2 * i + 1)
        root.right = insert_level_order(arr, 2 * i + 2)
        return root

    # Test Case 1
    root = insert_level_order([3, 1, 4, None, 2])
    k = 1
    print("Test Case 1:", solution.kthSmallest(root, k))  # Output: 1

    # Test Case 2
    root = insert_level_order([5, 3, 6, 2, 4, None, None, 1])
    k = 3
    print("Test Case 2:", solution.kthSmallest(root, k))  # Output: 3

if __name__ == "__main__":
    main()
