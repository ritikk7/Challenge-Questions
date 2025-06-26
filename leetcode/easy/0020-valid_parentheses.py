# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use a stack to match opening brackets with their corresponding closing brackets using a hashmap.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:
            if c in char_map and stack:
                start = stack.pop()
                if char_map[c] != start:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    s = "()"
    print("Test Case 1:", solution.isValid(s))  # Output: True

    # Test Case 2
    s = "()[]{}"
    print("Test Case 2:", solution.isValid(s))  # Output: True

    # Test Case 3
    s = "(]"
    print("Test Case 3:", solution.isValid(s))  # Output: False

if __name__ == "__main__":
    main()
