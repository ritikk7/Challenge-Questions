# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Use a sliding window approach with a set to track unique characters in the current substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Test cases
def main():
    solution = Solution()
    
    # Test Case 1
    s = "abcabcbb"
    print("Test Case 1:", solution.lengthOfLongestSubstring(s))  # Output: 3
    
    # Test Case 2
    s = "bbbbb"
    print("Test Case 2:", solution.lengthOfLongestSubstring(s))  # Output: 1
    
    # Test Case 3
    s = "pwwkew"
    print("Test Case 3:", solution.lengthOfLongestSubstring(s))  # Output: 3

if __name__ == "__main__":
    main()
