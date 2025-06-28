# Problem: Count Alternating Subarrays
# Link: https://leetcode.com/problems/count-alternating-subarrays/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Use two pointers to track maximal alternating segments. For each such segment, compute the number of subarrays.

from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        total = 0

        for r in range(n):
            if r == n - 1 or nums[r] == nums[r + 1]:
                m = r - l + 1
                total += (m * (m + 1)) // 2
                l = r + 1
        
        return total

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1, 0, 1, 0]
    print("Test Case 1:", solution.countAlternatingSubarrays(nums))  # Output: 10

    # Test Case 2
    nums = [0, 1, 1, 1]
    print("Test Case 2:", solution.countAlternatingSubarrays(nums))  # Output: 5

    # Test Case 3
    nums = [0]
    print("Test Case 3:", solution.countAlternatingSubarrays(nums))  # Output: 1

if __name__ == "__main__":
    main()
