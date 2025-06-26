# Problem: Binary Tree Paths
# Link: https://leetcode.com/problems/binary-tree-paths/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use DFS to track the path from root to each leaf. Append valid paths to the output list.

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []

        def helper(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                output.append("->".join(path))
            else:
                helper(node.left, path)
                helper(node.right, path)

            path.pop()

        helper(root, [])
        return output

# Test cases
def main():
    solution = Solution()

    # Build test tree: [1, 2, 3, None, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print("Test Case 1:", solution.binaryTreePaths(root))  # Output: ["1->2->5", "1->3"]

    # Test Case 2: Single node
    root = TreeNode(1)
    print("Test Case 2:", solution.binaryTreePaths(root))  # Output: ["1"]

if __name__ == "__main__":
    main()
