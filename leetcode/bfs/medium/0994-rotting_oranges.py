# Problem: Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium
# Time complexity: O(m * n), where m is the number of rows and n is the number of columns
# Space complexity: O(m * n), for the queue used in BFS

# Solution: Use BFS starting from all initially rotten oranges.
# At each level (minute), rot all adjacent fresh oranges.
# Track time as BFS levels and count fresh oranges. If any remain after BFS, return -1.

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0

        while rotten and fresh > 0:
            rotten_count = len(rotten)
            time += 1
            for _ in range(rotten_count):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        rotten.append((nr, nc))
                        fresh -= 1              
                        grid[nr][nc] = 2

        return -1 if fresh > 0 else time

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("Test Case 1:", solution.orangesRotting(grid))  # Output: 4

    # Test Case 2
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print("Test Case 2:", solution.orangesRotting(grid))  # Output: -1

    # Test Case 3
    grid = [[0,2]]
    print("Test Case 3:", solution.orangesRotting(grid))  # Output: 0

    # Test Case 4
    grid = [[1]]
    print("Test Case 4:", solution.orangesRotting(grid))  # Output: -1

    # Test Case 5
    grid = [[2,2,2,1]]
    print("Test Case 5:", solution.orangesRotting(grid))  # Output: 1

if __name__ == "__main__":
    main()
