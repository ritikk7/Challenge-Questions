# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Use two pointers approach, starting at both ends of the array and moving the pointer with the smaller height.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        
        while right > left:
            minHeight = min(height[left], height[right])
            base = right - left
            vol = base * minHeight
            result = max(result, vol)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return result

# Test cases
def main():
    solution = Solution()
    
    # Test Case 1
    height = [1,8,6,2,5,4,8,3,7]
    print("Test Case 1:", solution.maxArea(height))  # Output: 49
    
    # Test Case 2
    height = [1,1]
    print("Test Case 2:", solution.maxArea(height))  # Output: 1
    
    # Test Case 3
    height = [4,3,2,1,4]
    print("Test Case 3:", solution.maxArea(height))  # Output: 16

if __name__ == "__main__":
    main()
