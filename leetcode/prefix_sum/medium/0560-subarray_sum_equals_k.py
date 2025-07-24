# Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use a hashmap to store prefix sums and track how many times each sum occurs to efficiently count valid subarrays.

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        res = 0
        running = 0

        for num in nums:
            running += num
            if running - k in prefix_sums:
                res += prefix_sums[running - k]
            prefix_sums[running] = prefix_sums.get(running, 0) + 1

        return res

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1,1,1]
    k = 2
    print("Test Case 1:", solution.subarraySum(nums, k))  # Output: 2

    # Test Case 2
    nums = [1,2,3]
    k = 3
    print("Test Case 2:", solution.subarraySum(nums, k))  # Output: 2

    # Test Case 3
    nums = [1]
    k = 0
    print("Test Case 3:", solution.subarraySum(nums, k))  # Output: 0

if __name__ == "__main__":
    main()
