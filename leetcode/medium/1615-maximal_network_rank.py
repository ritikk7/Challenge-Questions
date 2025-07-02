# Problem: Maximal Network Rank
# Link: https://leetcode.com/problems/maximal-network-rank/description/
# Difficulty: Medium
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Solution: Build an adjacency set for each city, then compute network rank for every city pair considering shared roads.

from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]

        for c1, c2 in roads:
            adj[c1].add(c2)
            adj[c2].add(c1)

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = len(adj[i]) + len(adj[j])
                if j in adj[i]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    print("Test Case 1:", solution.maximalNetworkRank(n, roads))  # Output: 4

    # Test Case 2
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    print("Test Case 2:", solution.maximalNetworkRank(n, roads))  # Output: 5

    # Test Case 3
    n = 2
    roads = [[0,1]]
    print("Test Case 3:", solution.maximalNetworkRank(n, roads))  # Output: 1

if __name__ == "__main__":
    main()
