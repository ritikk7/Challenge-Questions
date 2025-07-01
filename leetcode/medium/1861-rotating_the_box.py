# Problem: Rotate the Box
# Link: https://leetcode.com/problems/rotate-the-box/description/
# Difficulty: Medium
# Time complexity: O(m * n)
# Space complexity: O(m * n)

# Solution: Rotate the box 90 degrees clockwise, then simulate gravity by shifting stones down in each column.

from typing import List
from collections import deque

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        output = [["" for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                output[j][m - 1 - i] = boxGrid[i][j]

        for col in range(m):
            empty = deque()
            for row in range(n - 1, -1, -1):
                if output[row][col] == ".":
                    empty.append((row, col))
                elif output[row][col] == "*":
                    empty.clear()
                elif output[row][col] == "#":
                    if empty:
                        y, x = empty.popleft()
                        output[y][x] = "#"
                        output[row][col] = "."
                        empty.append((row, col))

        return output

# Test cases
def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def main():
    solution = Solution()

    # Test Case 1
    box = [
        ["#",".","#"]
    ]
    print("Test Case 1:")
    print_grid(solution.rotateTheBox(box))  # Output: [['.'], ['#'], ['#']]

    # Test Case 2
    box = [
        ["#",".","*","."],
        ["#","#","*","."]
    ]
    print("Test Case 2:")
    print_grid(solution.rotateTheBox(box))  # Expected rotated and gravity-applied result

    # Test Case 3
    box = [
        ["*","#","*","."]
    ]
    print("Test Case 3:")
    print_grid(solution.rotateTheBox(box))  # Expected rotated and gravity-applied result

if __name__ == "__main__":
    main()
