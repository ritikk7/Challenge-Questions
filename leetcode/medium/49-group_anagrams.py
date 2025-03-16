# Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/description/
# Difficulty: Medium
# Time complexity: O(n * k log k) where n = number of strings and k = maximum length of a string
# Space complexity: O(nk)

# Solution: Use a hashmap where the key is the sorted version of each string, grouping all anagrams under the same key.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for x in strs:
            y = ''.join(sorted(x))
            if y in mydict:
                mydict[y].append(x)
            else:
                mydict[y] = [x]

        return list(mydict.values())

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Test Case 1:", solution.groupAnagrams(strs))  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    # Test Case 2
    strs = [""]
    print("Test Case 2:", solution.groupAnagrams(strs))  # Output: [[""]]

    # Test Case 3
    strs = ["a"]
    print("Test Case 3:", solution.groupAnagrams(strs))  # Output: [["a"]]

if __name__ == "__main__":
    main()
