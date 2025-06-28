# Problem: K-diff Pairs in an Array
# Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use a set to track seen numbers and another set to track valid unique pairs.

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        pairs = set()

        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))
            if num + k in seen:
                pairs.add((num, num + k))
            seen.add(num)

        return len(pairs)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [3, 1, 4, 1, 5]
    k = 2
    print("Test Case 1:", solution.findPairs(nums, k))  # Output: 2

    # Test Case 2
    nums = [1, 2, 3, 4, 5]
    k = 1
    print("Test Case 2:", solution.findPairs(nums, k))  # Output: 4

    # Test Case 3
    nums = [1, 3, 1, 5, 4]
    k = 0
    print("Test Case 3:", solution.findPairs(nums, k))  # Output: 1

if __name__ == "__main__":
    main()
