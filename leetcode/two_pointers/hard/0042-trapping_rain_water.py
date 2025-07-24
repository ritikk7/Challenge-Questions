# Problem: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
# Time complexity: O(n), where n is the number of bars
# Space complexity: O(1), using two-pointer technique with constant space

# Solution: Use two pointers starting from both ends.
# Track the max height seen from both left and right.
# Water is trapped based on the shorter max boundary at each step.
# Add trapped water by subtracting the current bar height from the min boundary height.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        water = 0

        while l < r:
            if l_max <= r_max:
                l += 1
                l_max = max(l_max, height[l])
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]

        return water

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Test Case 1:", solution.trap(height))  # Output: 6

    # Test Case 2
    height = [4,2,0,3,2,5]
    print("Test Case 2:", solution.trap(height))  # Output: 9

    # Test Case 3
    height = [1,0,1]
    print("Test Case 3:", solution.trap(height))  # Output: 1

    # Test Case 4
    height = [2,0,2]
    print("Test Case 4:", solution.trap(height))  # Output: 2

    # Test Case 5
    height = [3, 0, 0, 2, 0, 4]
    print("Test Case 5:", solution.trap(height))  # Output: 10

if __name__ == "__main__":
    main()
