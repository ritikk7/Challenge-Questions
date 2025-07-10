# Problem: Minimum Path Sum
# Link: https://leetcode.com/problems/minimum-path-sum/
# Difficulty: Medium
# Time complexity: O(m * n), where m is the number of rows and n is the number of columns
# Space complexity: O(m * n), due to the auxiliary DP table used

# Solution: Use dynamic programming to build a sum grid from top-left to bottom-right.
# Each cell holds the minimum sum to reach that point from the start.
# We take the minimum of coming from the top or left neighbor.

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sum_grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    sum_grid[i][j] = grid[i][j]
                elif i == 0:
                    sum_grid[i][j] = grid[i][j] + sum_grid[i][j - 1]
                elif j == 0:
                    sum_grid[i][j] = grid[i][j] + sum_grid[i - 1][j]
                else:
                    sum_grid[i][j] = grid[i][j] + min(sum_grid[i][j - 1], sum_grid[i - 1][j])
        
        return sum_grid[-1][-1]

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print("Test Case 1:", solution.minPathSum(grid))  # Output: 7

    # Test Case 2
    grid = [[1,2,3],[4,5,6]]
    print("Test Case 2:", solution.minPathSum(grid))  # Output: 12

    # Test Case 3
    grid = [[5]]
    print("Test Case 3:", solution.minPathSum(grid))  # Output: 5

    # Test Case 4
    grid = [[1,2],[1,1]]
    print("Test Case 4:", solution.minPathSum(grid))  # Output: 3

if __name__ == "__main__":
    main()
