# Problem: Rotate Image
# Link: https://leetcode.com/problems/rotate-image/description/
# Difficulty: Medium
# Time complexity: O(n^2)
# Space complexity: O(1)

# Solution: First transpose the matrix, then reverse each row to rotate the matrix 90 degrees clockwise in-place.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def main():
    solution = Solution()

    # Test Case 1
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(matrix)
    print("Test Case 1:")
    print_matrix(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

    # Test Case 2
    matrix = [
        [5, 1, 9,11],
        [2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    solution.rotate(matrix)
    print("Test Case 2:")
    print_matrix(matrix)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    # Test Case 3
    matrix = [[1]]
    solution.rotate(matrix)
    print("Test Case 3:")
    print_matrix(matrix)  # Output: [[1]]

if __name__ == "__main__":
    main()
