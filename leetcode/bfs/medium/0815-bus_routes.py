# Problem: Bus Routes
# Link: https://leetcode.com/problems/bus-routes/
# Difficulty: Medium
# Time complexity: O(n * k), where n is the number of routes and k is the average number of stops per route
# Space complexity: O(n + m), where n is the number of routes and m is the number of unique stops

# Solution: Use BFS starting from the source stop. At each level, traverse all routes from current stops.
# Track visited routes to prevent re-processing and visited stops to avoid cycles.
# Each BFS level corresponds to taking an additional bus.

from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        m = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                m[stop].add(i)
        
        queue = deque()
        queue.append(source)
        visited_routes = set()
        visited_stops = set()
        result = 0

        while queue:
            for _ in range(len(queue)):
                curr_stop = queue.popleft()
                visited_stops.add(curr_stop)

                if curr_stop == target:
                    return result

                for route in m[curr_stop]:
                    if route not in visited_routes:
                        visited_routes.add(route)
                        for stop in routes[route]:
                            if stop not in visited_stops:
                                queue.append(stop)

            result += 1
        
        return -1

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    print("Test Case 1:", solution.numBusesToDestination(routes, source, target))  # Output: 2

    # Test Case 2
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    print("Test Case 2:", solution.numBusesToDestination(routes, source, target))  # Output: -1

    # Test Case 3
    routes = [[1,2,3,4,5,6,7,8,9,10]]
    source = 1
    target = 10
    print("Test Case 3:", solution.numBusesToDestination(routes, source, target))  # Output: 1

    # Test Case 4
    routes = [[1,7],[3,5]]
    source = 5
    target = 5
    print("Test Case 4:", solution.numBusesToDestination(routes, source, target))  # Output: 0

if __name__ == "__main__":
    main()
