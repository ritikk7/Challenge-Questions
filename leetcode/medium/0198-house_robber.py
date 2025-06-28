# Problem: House Robber
# Link: https://leetcode.com/problems/house-robber/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use dynamic programming to track maximum money robbed up to each house, considering non-adjacent constraints.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        money = [0] * n
        money[0] = nums[0]
        money[1] = nums[1]
        money[2] = nums[2] + money[0]
        
        for house in range(3, n):
            money[house] = nums[house] + max(money[house - 2], money[house - 3])

        return max(money[-1], money[-2])

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1, 2, 3, 1]
    print("Test Case 1:", solution.rob(nums))  # Output: 4

    # Test Case 2
    nums = [2, 7, 9, 3, 1]
    print("Test Case 2:", solution.rob(nums))  # Output: 12

    # Test Case 3
    nums = [2, 1, 1, 2]
    print("Test Case 3:", solution.rob(nums))  # Output: 4

if __name__ == "__main__":
    main()
