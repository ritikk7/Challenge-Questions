# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Apply Kadane's algorithm to keep track of the maximum subarray sum ending at each position.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        max_so_far = nums[0]

        for i in range(1, n):
            curr = nums[i]
            max_so_far = max(max_so_far + curr, curr)
            max_sum = max(max_so_far, max_sum)

        return max_sum

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("Test Case 1:", solution.maxSubArray(nums))  # Output: 6

    # Test Case 2
    nums = [1]
    print("Test Case 2:", solution.maxSubArray(nums))  # Output: 1

    # Test Case 3
    nums = [5,4,-1,7,8]
    print("Test Case 3:", solution.maxSubArray(nums))  # Output: 23

if __name__ == "__main__":
    main()
