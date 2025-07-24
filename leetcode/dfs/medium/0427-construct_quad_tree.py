# Problem: Construct Quad Tree
# Link: https://leetcode.com/problems/construct-quad-tree/
# Difficulty: Medium
# Time complexity: O(n²), where n is the size of the grid (since every cell might be visited once)
# Space complexity: O(log n) recursion stack (or up to O(n²) if every cell becomes a separate node)

# Solution: Use a recursive DFS approach to divide the grid into quadrants.
# If all four quadrants are leaves with the same value, merge them into one leaf node.
# Otherwise, return a non-leaf node with children.

from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def buildTree(x, y, size):
            if size == 1:
                return Node(grid[x][y] == 1, True)

            topLeft = buildTree(x, y, size // 2)
            topRight = buildTree(x, y + size // 2, size // 2)
            bottomLeft = buildTree(x + size // 2, y, size // 2)
            bottomRight = buildTree(x + size // 2, y + size // 2, size // 2)
            
            children = [topLeft, topRight, bottomLeft, bottomRight]
            areLeaf = True
            sameValue = True

            for child in children:
                if not child.isLeaf:
                    areLeaf = False
                if child.val != topLeft.val:
                    sameValue = False

            if areLeaf and sameValue:
                return Node(topLeft.val, True)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return buildTree(0, 0, len(grid))

# Test cases
def main():
    solution = Solution()

    def printTree(node):
        if node.isLeaf:
            return f"Leaf({int(node.val)})"
        return f"Node({printTree(node.topLeft)}, {printTree(node.topRight)}, {printTree(node.bottomLeft)}, {printTree(node.bottomRight)})"

    # Test Case 1
    grid = [[0, 1], [1, 0]]
    root = solution.construct(grid)
    print("Test Case 1:", printTree(root))  # Output: a non-leaf node with four children

    # Test Case 2
    grid = [[1, 1], [1, 1]]
    root = solution.construct(grid)
    print("Test Case 2:", printTree(root))  # Output: Leaf(1)

    # Test Case 3
    grid = [[0]]
    root = solution.construct(grid)
    print("Test Case 3:", printTree(root))  # Output: Leaf(0)

if __name__ == "__main__":
    main()
