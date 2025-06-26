# Problem: Course Schedule II
# Link: https://leetcode.com/problems/course-schedule-ii/description/
# Difficulty: Medium
# Time complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
# Space complexity: O(V + E)

# Solution: Perform topological sort using DFS. Detect cycles during DFS to ensure a valid ordering exists.

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        stack = []

        def search(course):
            if visited[course] == 1:
                return False  # cycle detected
            if visited[course] == 2:
                return True

            visited[course] = 1
            for next_course in adjList[course]:
                if not search(next_course):
                    return False
            visited[course] = 2
            stack.append(course)
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not search(course):
                    return []

        return stack[::-1]

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print("Test Case 1:", solution.findOrder(numCourses, prerequisites))  # Output: [0, 1]

    # Test Case 2
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print("Test Case 2:", solution.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]

    # Test Case 3
    numCourses = 1
    prerequisites = []
    print("Test Case 3:", solution.findOrder(numCourses, prerequisites))  # Output: [0]

if __name__ == "__main__":
    main()
