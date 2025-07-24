# Problem: Find N Unique Integers Sum up to Zero
# Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Construct pairs of positive and negative integers, append 0 if n is odd.

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)

        if n % 2 != 0:
            res.append(0)

        return res

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    n = 5
    print("Test Case 1:", solution.sumZero(n))  # Output: [1,-1,2,-2,0] (order may vary)

    # Test Case 2
    n = 3
    print("Test Case 2:", solution.sumZero(n))  # Output: [1,-1,0]

    # Test Case 3
    n = 4
    print("Test Case 3:", solution.sumZero(n))  # Output: [1,-1,2,-2]

if __name__ == "__main__":
    main()
