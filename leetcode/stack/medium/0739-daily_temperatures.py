# Problem: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Time complexity: O(n), where n is the number of days (each index is pushed and popped at most once)
# Space complexity: O(n), for the result array and the stack

# Solution: Use a monotonic decreasing stack that stores indices of unresolved temperatures.
# For each temperature, if it's higher than the one at the top of the stack, resolve the previous index.
# Store the difference in days in the answer array.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0 for _ in range(n)]
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Test Case 1:", solution.dailyTemperatures(temperatures))  # Output: [1,1,4,2,1,1,0,0]

    # Test Case 2
    temperatures = [30, 40, 50, 60]
    print("Test Case 2:", solution.dailyTemperatures(temperatures))  # Output: [1,1,1,0]

    # Test Case 3
    temperatures = [30, 60, 90]
    print("Test Case 3:", solution.dailyTemperatures(temperatures))  # Output: [1,1,0]

    # Test Case 4
    temperatures = [90, 80, 70, 60]
    print("Test Case 4:", solution.dailyTemperatures(temperatures))  # Output: [0,0,0,0]

    # Test Case 5
    temperatures = [70]
    print("Test Case 5:", solution.dailyTemperatures(temperatures))  # Output: [0]

if __name__ == "__main__":
    main()
