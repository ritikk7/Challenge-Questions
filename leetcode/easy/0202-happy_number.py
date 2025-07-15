# Problem: Happy Number
# Link: https://leetcode.com/problems/happy-number/
# Difficulty: Easy
# Time complexity: O(log n), for each sum of squares operation; total time is O(cycle length)
# Space complexity: O(1), using Floyd's Cycle Detection

# Solution: Use Floyd's cycle detection algorithm (slow and fast pointers) to detect cycles.
# Define a helper function that computes the sum of squares of digits.
# If we ever reach 1, the number is happy. If a cycle forms before that, it's not.

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            digits = []
            while n > 9:
                digits.append(n % 10)
                n = n // 10
            digits.append(n)

            total = 0
            for digit in digits:
                total += digit * digit
            return total
        
        slow = n
        fast = n

        while fast != 1:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

            if slow == fast and fast != 1:
                return False
        
        return True

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    n = 19
    print("Test Case 1:", solution.isHappy(n))  # Output: True

    # Test Case 2
    n = 2
    print("Test Case 2:", solution.isHappy(n))  # Output: False

    # Test Case 3
    n = 1
    print("Test Case 3:", solution.isHappy(n))  # Output: True

    # Test Case 4
    n = 7
    print("Test Case 4:", solution.isHappy(n))  # Output: True

    # Test Case 5
    n = 20
    print("Test Case 5:", solution.isHappy(n))  # Output: False

if __name__ == "__main__":
    main()
