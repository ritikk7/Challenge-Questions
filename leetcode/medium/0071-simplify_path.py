# Problem: Simplify Path
# Link: https://leetcode.com/problems/simplify-path/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Split the path by '/', handle "." and ".." tokens appropriately using a stack to construct the canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        canonical = []

        for token in tokens:
            if not token or token == ".":
                continue
            elif token == "..":
                if canonical:
                    canonical.pop()
            else:
                canonical.append(token)

        return "/" + "/".join(canonical)

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    path = "/home/"
    print("Test Case 1:", solution.simplifyPath(path))  # Output: "/home"

    # Test Case 2
    path = "/../"
    print("Test Case 2:", solution.simplifyPath(path))  # Output: "/"

    # Test Case 3
    path = "/home//foo/"
    print("Test Case 3:", solution.simplifyPath(path))  # Output: "/home/foo"

if __name__ == "__main__":
    main()
