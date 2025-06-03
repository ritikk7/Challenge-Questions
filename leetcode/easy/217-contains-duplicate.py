# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Convert the list to a set and compare lengths to check for duplicates.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(unique) != len(nums)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1, 2, 3, 1]
    print("Test Case 1:", solution.containsDuplicate(nums))  # Output: True

    # Test Case 2
    nums = [1, 2, 3, 4]
    print("Test Case 2:", solution.containsDuplicate(nums))  # Output: False

    # Test Case 3
    nums = [1,1,1,3,3,4,3,2,4,2]
    print("Test Case 3:", solution.containsDuplicate(nums))  # Output: True

if __name__ == "__main__":
    main()
