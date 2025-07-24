# Problem: Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/description/
# Difficulty: Medium
# Time complexity: O(n log n)
# Space complexity: O(n)

# Solution: Sort intervals by start time and merge overlapping ones by comparing the current with the last merged interval.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        if n < 2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        merged_intervals = [intervals[0]]

        for i in range(1, n):
            first = merged_intervals[-1]
            second = intervals[i]

            if second[0] <= first[1]:
                if second[1] <= first[1]:
                    continue
                new = (first[0], second[1])
                merged_intervals.pop()
                merged_intervals.append(new)
            else:
                merged_intervals.append(second)
        
        return merged_intervals

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Test Case 1:", solution.merge(intervals))  # Output: [[1,6],[8,10],[15,18]]

    # Test Case 2
    intervals = [[1,4],[4,5]]
    print("Test Case 2:", solution.merge(intervals))  # Output: [[1,5]]

    # Test Case 3
    intervals = [[1,4],[0,2],[3,5]]
    print("Test Case 3:", solution.merge(intervals))  # Output: [[0,5]]

if __name__ == "__main__":
    main()
