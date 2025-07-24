# Problem: N-ary Tree Level Order Traversal
# Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Difficulty: Medium
# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), for the queue used in level-order traversal and the result list

# Solution: Use BFS (queue) to traverse the tree level by level.
# At each level, collect all child node values and enqueue the child nodes for the next level.

from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                for child in curr.children:
                    queue.append(child)
            result.append(level)

        return result

# Test cases
def main():
    solution = Solution()

    # Helper to build a sample N-ary tree
    def build_tree():
        # Tree:
        #         1
        #      /  |  \
        #     3   2   4
        #   /  \
        #  5    6
        node5 = Node(5)
        node6 = Node(6)
        node3 = Node(3, [node5, node6])
        node2 = Node(2)
        node4 = Node(4)
        root = Node(1, [node3, node2, node4])
        return root

    # Test Case 1
    root = build_tree()
    print("Test Case 1:", solution.levelOrder(root))  # Output: [[1], [3,2,4], [5,6]]

    # Test Case 2: Single node
    root = Node(10)
    print("Test Case 2:", solution.levelOrder(root))  # Output: [[10]]

    # Test Case 3: Empty tree
    root = None
    print("Test Case 3:", solution.levelOrder(root))  # Output: []

if __name__ == "__main__":
    main()
