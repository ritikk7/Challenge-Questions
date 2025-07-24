# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Time complexity: O(n log n + m), where n is the number of strings and m is the length of the shortest string
# Space complexity: O(m), for storing the prefix result

# Solution: Sort the list of strings. The common prefix of the entire list must be a prefix of the first and last strings.
# Compare the first and last string character by character to find the common prefix.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                result.append(first[i])
            else:
                return "".join(result)

        return "".join(result)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    strs = ["flower","flow","flight"]
    print("Test Case 1:", solution.longestCommonPrefix(strs))  # Output: "fl"

    # Test Case 2
    strs = ["dog","racecar","car"]
    print("Test Case 2:", solution.longestCommonPrefix(strs))  # Output: ""

    # Test Case 3
    strs = ["interspecies","interstellar","interstate"]
    print("Test Case 3:", solution.longestCommonPrefix(strs))  # Output: "inters"

    # Test Case 4
    strs = ["a"]
    print("Test Case 4:", solution.longestCommonPrefix(strs))  # Output: "a"

    # Test Case 5
    strs = ["ab", "a"]
    print("Test Case 5:", solution.longestCommonPrefix(strs))  # Output: "a"

if __name__ == "__main__":
    main()
