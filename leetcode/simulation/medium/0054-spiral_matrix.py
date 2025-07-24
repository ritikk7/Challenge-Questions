# Problem: Spiral Matrix
# Link: https://leetcode.com/problems/spiral-matrix/description/
# Difficulty: Medium
# Time complexity: O(m * n)
# Space complexity: O(1) excluding output list

# Solution: Traverse the matrix in spiral order by marking visited cells, changing direction when needed.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        r, c = len(matrix), len(matrix[0])
        i, j = 0, 0
        state = 0  # 0 = right, 1 = down, 2 = left, 3 = up
        total = r * c

        while len(output) < total:
            output.append(matrix[i][j])
            matrix[i][j] = False

            ni, nj = i, j
            if state == 0: nj += 1
            elif state == 1: ni += 1
            elif state == 2: nj -= 1
            elif state == 3: ni -= 1

            if ni < 0 or ni >= r or nj < 0 or nj >= c or matrix[ni][nj] is False:
                state = (state + 1) % 4
                if state == 0: j += 1
                elif state == 1: i += 1
                elif state == 2: j -= 1
                elif state == 3: i -= 1
            else:
                i, j = ni, nj

        return output

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test Case 1:", solution.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]

    # Test Case 2
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    print("Test Case 2:", solution.spiralOrder(matrix))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    # Test Case 3
    matrix = [[1]]
    print("Test Case 3:", solution.spiralOrder(matrix))  # Output: [1]

if __name__ == "__main__":
    main()
