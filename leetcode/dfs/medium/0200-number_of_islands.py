# Problem: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/description/
# Difficulty: Medium
# Time complexity: O(m * n)
# Space complexity: O(m * n)

# Solution: Use BFS to traverse each island, marking visited land cells as water to avoid revisits.

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        total = 0

        def findIsland(coord):
            queue = deque()
            queue.append(coord)

            while queue:
                x, y = queue.popleft()

                for d in directions:
                    xd, yd = x + d[0], y + d[1]

                    if 0 <= xd < m and 0 <= yd < n and grid[xd][yd] == "1":
                        grid[xd][yd] = "0"
                        queue.append((xd, yd))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    findIsland((i, j))
                    total += 1

        return total

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Test Case 1:", solution.numIslands(grid))  # Output: 1

    # Test Case 2
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Test Case 2:", solution.numIslands(grid))  # Output: 3

    # Test Case 3
    grid = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    print("Test Case 3:", solution.numIslands(grid))  # Output: 0

if __name__ == "__main__":
    main()
