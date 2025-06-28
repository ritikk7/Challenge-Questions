# Problem: Reverse String
# Link: https://leetcode.com/problems/reverse-string/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Use two pointers to swap characters from both ends of the string in-place.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    s = ["h","e","l","l","o"]
    solution.reverseString(s)
    print("Test Case 1:", s)  # Output: ['o','l','l','e','h']

    # Test Case 2
    s = ["H","a","n","n","a","h"]
    solution.reverseString(s)
    print("Test Case 2:", s)  # Output: ['h','a','n','n','a','H']

    # Test Case 3
    s = ["a"]
    solution.reverseString(s)
    print("Test Case 3:", s)  # Output: ['a']

if __name__ == "__main__":
    main()
