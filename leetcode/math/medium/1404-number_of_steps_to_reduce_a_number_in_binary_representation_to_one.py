# Problem: Number of Steps to Reduce a Number in Binary Representation to One
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Difficulty: Medium
# Time complexity: O(n), where n is the length of the binary string
# Space complexity: O(n), due to the list conversion of the string

# Solution: Simulate binary reduction:
# - If the last digit is 0, divide by 2 (pop the last character).
# - If the last digit is 1, simulate addition by 1: flip trailing 1s to 0s and handle carry.
# Keep doing this until the binary string becomes "1".

class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        s = list(s)

        while len(s) > 1:
            if s[-1] == '0':
                s.pop()
            else:
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i < 0:
                    s = ['1'] + s
                else:
                    s[i] = '1'

            result += 1

        return result

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    s = "1101"
    print("Test Case 1:", solution.numSteps(s))  # Output: 6

    # Test Case 2
    s = "10"
    print("Test Case 2:", solution.numSteps(s))  # Output: 1

    # Test Case 3
    s = "1"
    print("Test Case 3:", solution.numSteps(s))  # Output: 0

    # Test Case 4
    s = "1111011110000011100000110001011011110010111001010111110001"
    print("Test Case 4:", solution.numSteps(s))  # Output: Large number of steps (performance check)

if __name__ == "__main__":
    main()
