# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use a hashmap to store the complement of the current number and check if it exists in the hashmap

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Test Case 1:", solution.twoSum(nums, target))  # Output: [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print("Test Case 2:", solution.twoSum(nums, target))  # Output: [1, 2]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print("Test Case 3:", solution.twoSum(nums, target))  # Output: [0, 1]

if __name__ == "__main__":
    main()
