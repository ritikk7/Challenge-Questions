# Problem: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Loop through the string, add or subtract based on comparison with next Roman numeral.

class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        num = 0
        n = len(s)

        for i in range(n):
            current = num_map[s[i]]
            if i + 1 < n and num_map[s[i + 1]] > current:
                num -= current
            else:
                num += current
        
        return num

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    s = "III"
    print("Test Case 1:", solution.romanToInt(s))  # Output: 3

    # Test Case 2
    s = "IV"
    print("Test Case 2:", solution.romanToInt(s))  # Output: 4

    # Test Case 3
    s = "MCMXCIV"
    print("Test Case 3:", solution.romanToInt(s))  # Output: 1994

if __name__ == "__main__":
    main()
