# Problem: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Difficulty: Medium
# Time complexity: O(log n + k), where k is the number of target duplicates
# Space complexity: O(1)

# Solution: Perform binary search to locate the target, then expand linearly to find bounds. Alternative versions do pure binary search twice.

from typing import List
from collections import deque

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        q = deque([(0, n)])

        while q:
            l, r = q.popleft()
            if l >= r:
                continue
            m = (l + r) // 2

            if nums[m] == target:
                start, end = m, m
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < n and nums[end] == target:
                    end += 1
                return [start + 1, end - 1]
            elif nums[m] < target:
                q.append((m + 1, r))
            elif nums[m] > target:
                q.append((l, m))

        return [-1, -1]

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [5,7,7,8,8,10]
    target = 8
    print("Test Case 1:", solution.searchRange(nums, target))  # Output: [3, 4]

    # Test Case 2
    nums = [5,7,7,8,8,10]
    target = 6
    print("Test Case 2:", solution.searchRange(nums, target))  # Output: [-1, -1]

    # Test Case 3
    nums = []
    target = 0
    print("Test Case 3:", solution.searchRange(nums, target))  # Output: [-1, -1]

if __name__ == "__main__":
    main()
