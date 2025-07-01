# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/description/
# Difficulty: Medium
# Time complexity: O(n^2)
# Space complexity: O(n) for sorting output

# Solution: Sort the array, fix one number, and use a two-pointer approach to find pairs that sum to the target.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    triplets.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return triplets

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [-1, 0, 1, 2, -1, -4]
    print("Test Case 1:", solution.threeSum(nums))  # Output: [[-1,-1,2], [-1,0,1]]

    # Test Case 2
    nums = [0, 1, 1]
    print("Test Case 2:", solution.threeSum(nums))  # Output: []

    # Test Case 3
    nums = [0, 0, 0]
    print("Test Case 3:", solution.threeSum(nums))  # Output: [[0,0,0]]

if __name__ == "__main__":
    main()
