# Problem: Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/
# Difficulty: Medium
# Time complexity: O(n log n), where n is the length of the string (due to sorting the characters by frequency)
# Space complexity: O(n), for storing the frequency map and result array

# Solution: Count the frequency of each character. If any character exceeds (n+1)//2, it's impossible to reorganize.
# Otherwise, place the most frequent characters first at even indices, then fill the odd indices.

from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        
        sorted_keys = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        result = [''] * len(s)
        index = 0

        for key in sorted_keys:
            for _ in range(freq[key]):
                result[index] = key
                index += 2
                if index >= len(s):
                    index = 1

        return ''.join(result)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    s = "aab"
    print("Test Case 1:", solution.reorganizeString(s))  # Output: "aba"

    # Test Case 2
    s = "aaab"
    print("Test Case 2:", solution.reorganizeString(s))  # Output: "" (not possible)

    # Test Case 3
    s = "vvvlo"
    print("Test Case 3:", solution.reorganizeString(s))  # Output: e.g. "vlvov" or any valid reorg

    # Test Case 4
    s = "a"
    print("Test Case 4:", solution.reorganizeString(s))  # Output: "a"

if __name__ == "__main__":
    main()
