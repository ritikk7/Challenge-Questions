# Problem: Count Primes
# Link: https://leetcode.com/problems/count-primes/description/
# Difficulty: Medium
# Time complexity: O(n log log n)
# Space complexity: O(n)

# Solution: Use the Sieve of Eratosthenes to efficiently count prime numbers less than n.

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
 
        primes = [True] * n
        primes[0], primes[1] = False, False
        
        sqrt = int(math.sqrt(n)) + 1
        
        for num in range(2, sqrt):
            if primes[num]:
                for i in range(num * 2, n, num):
                    primes[i] = False

        return sum(primes)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    n = 10
    print("Test Case 1:", solution.countPrimes(n))  # Output: 4

    # Test Case 2
    n = 0
    print("Test Case 2:", solution.countPrimes(n))  # Output: 0

    # Test Case 3
    n = 1
    print("Test Case 3:", solution.countPrimes(n))  # Output: 0

if __name__ == "__main__":
    main()
