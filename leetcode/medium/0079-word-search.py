# Problem: Word Search
# Link: https://leetcode.com/problems/word-search/description/
# Difficulty: Medium
# Time complexity: O(m * n * 4^l), where m and n are the board dimensions and l is the length of the word
# Space complexity: O(l), where l is the length of the word (due to recursion and visited set)

# Solution: Perform DFS with backtracking from each cell. Use a visited set to avoid revisiting characters in the current path.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def track(r, c, idx, visited):
            if board[r][c] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if track(nr, nc, idx + 1, visited):
                        return True

            visited.remove((r, c))
            return False

        for i in range(rows):
            for j in range(cols):
                if track(i, j, 0, set()):
                    return True

        return False

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    print("Test Case 1:", solution.exist(board, word))  # Output: True

    # Test Case 2
    word = "SEE"
    print("Test Case 2:", solution.exist(board, word))  # Output: True

    # Test Case 3
    word = "ABCB"
    print("Test Case 3:", solution.exist(board, word))  # Output: False

if __name__ == "__main__":
    main()
