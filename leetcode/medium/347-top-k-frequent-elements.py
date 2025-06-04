# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Difficulty: Medium
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Count frequencies using a hashmap and then bucket sort the elements by frequency to extract the top K.

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = defaultdict(int)

        for num in nums:
            elements[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key in elements.keys():
            buckets[elements[key]].append(key)

        result = []

        for bucket in reversed(buckets):
            for val in bucket:
                result.append(val)
                k -= 1
                if k == 0:
                    return result

        return result

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    nums = [1,1,1,2,2,3]
    k = 2
    print("Test Case 1:", solution.topKFrequent(nums, k))  # Output: [1, 2]

    # Test Case 2
    nums = [1]
    k = 1
    print("Test Case 2:", solution.topKFrequent(nums, k))  # Output: [1]

    # Test Case 3
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print("Test Case 3:", solution.topKFrequent(nums, k))  # Output: [-1, 2]

if __name__ == "__main__":
    main()
