# Problem: Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Use a sliding window to find the minimum subarray length whose sum is at least the target.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        total = 0
        min_len = float('inf')

        while right < n and left <= right:
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1

        return 0 if min_len == float('inf') else min_len

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    target = 7
    nums = [2,3,1,2,4,3]
    print("Test Case 1:", solution.minSubArrayLen(target, nums))  # Output: 2

    # Test Case 2
    target = 4
    nums = [1,4,4]
    print("Test Case 2:", solution.minSubArrayLen(target, nums))  # Output: 1

    # Test Case 3
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print("Test Case 3:", solution.minSubArrayLen(target, nums))  # Output: 0

if __name__ == "__main__":
    main()
