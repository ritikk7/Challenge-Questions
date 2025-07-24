# Problem: Four Divisors
# Link: https://leetcode.com/problems/four-divisors/description/
# Difficulty: Medium
# Time complexity: O(n * sqrt(m)), where n = len(nums) and m = maximum value in nums
# Space complexity: O(1)

# Solution: For each number, find its divisors. If exactly four distinct divisors exist, add their sum to the total.

import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def findFourDivisors(num):
            divisors = set([1, num])

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:
                    return 0

            return sum(divisors) if len(divisors) == 4 else 0

        total = 0
        for num in nums:
            total += findFourDivisors(num)

        return total

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [21, 4, 7]
    print("Test Case 1:", solution.sumFourDivisors(nums))  # Output: 32

    # Test Case 2
    nums = [10, 15, 7]
    print("Test Case 2:", solution.sumFourDivisors(nums))  # Output: 42

    # Test Case 3
    nums = [28]
    print("Test Case 3:", solution.sumFourDivisors(nums))  # Output: 0

if __name__ == "__main__":
    main()
