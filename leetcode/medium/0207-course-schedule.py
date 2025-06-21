# Problem: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/description/
# Difficulty: Medium
# Time complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
# Space complexity: O(V + E)

# Solution: Use DFS to detect cycles in the directed graph represented by course prerequisites.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

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
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not search(course):
                    return False

        return True

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print("Test Case 1:", solution.canFinish(numCourses, prerequisites))  # Output: True

    # Test Case 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print("Test Case 2:", solution.canFinish(numCourses, prerequisites))  # Output: False

    # Test Case 3
    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print("Test Case 3:", solution.canFinish(numCourses, prerequisites))  # Output: True

if __name__ == "__main__":
    main()
