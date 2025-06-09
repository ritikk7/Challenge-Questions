# Problem: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Reverse the entire array, then reverse the first k elements and the rest separately.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    print("Test Case 1:", nums)  # Output: [5,6,7,1,2,3,4]

    # Test Case 2
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)
    print("Test Case 2:", nums)  # Output: [3,99,-1,-100]

    # Test Case 3
    nums = [1,2]
    k = 3
    solution.rotate(nums, k)
    print("Test Case 3:", nums)  # Output: [2,1]

if __name__ == "__main__":
    main()
