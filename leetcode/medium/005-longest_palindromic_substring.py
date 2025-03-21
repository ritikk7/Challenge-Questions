# Problem: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/
# Difficulty: Medium
# Time complexity: O(n^2)
# Space complexity: O(1)

# Solution: Use the expand-around-center approach to check for palindromic substrings centered at each index.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)   # Odd length palindrome
            if len(sub1) > len(result):
                result = sub1
            
            sub2 = expand(i, i+1) # Even length palindrome
            if len(sub2) > len(result):
                result = sub2
        
        return result

# Test cases
def main():
    solution = Solution()
    
    # Test Case 1
    s = "babad"
    print("Test Case 1:", solution.longestPalindrome(s))  # Output: "bab" or "aba"
    
    # Test Case 2
    s = "cbbd"
    print("Test Case 2:", solution.longestPalindrome(s))  # Output: "bb"
    
    # Test Case 3
    s = "a"
    print("Test Case 3:", solution.longestPalindrome(s))  # Output: "a"

if __name__ == "__main__":
    main()
