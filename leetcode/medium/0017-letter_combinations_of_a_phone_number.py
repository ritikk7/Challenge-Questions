# Problem: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Difficulty: Medium
# Time complexity: O(4^n), where n is the length of the input digits
# Space complexity: O(n) for recursion stack

# Solution: Use backtracking to generate all possible letter combinations based on phone keypad mapping.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        combinations = []

        def createCombo(combo, rem_digits):
            if not rem_digits:
                combinations.append(combo)
                return
            
            digit = rem_digits[0]

            for c in phone[int(digit)]:
                combo += c
                createCombo(combo, rem_digits[1:])
                combo = combo[:-1]

        createCombo("", digits)
        return combinations

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    digits = "23"
    print("Test Case 1:", solution.letterCombinations(digits))  # Output: All possible combinations of "23"

    # Test Case 2
    digits = ""
    print("Test Case 2:", solution.letterCombinations(digits))  # Output: []

    # Test Case 3
    digits = "2"
    print("Test Case 3:", solution.letterCombinations(digits))  # Output: ['a','b','c']

if __name__ == "__main__":
    main()
