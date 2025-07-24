# Problem: Cinema Seat Allocation
# Link: https://leetcode.com/problems/cinema-seat-allocation/description/
# Difficulty: Medium
# Time complexity: O(m), where m is the number of reserved seats
# Space complexity: O(m)

# Solution: Use a hashmap to track reserved seats per row. For each row, check the three possible 4-seat groups and compute maximum families.

from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res_seats = {}
        for row, col in reservedSeats:
            if row not in res_seats:
                res_seats[row] = set()
            res_seats[row].add(col)

        families = 0

        for row in res_seats:
            seats = res_seats[row]

            left = 2 in seats or 3 in seats or 4 in seats or 5 in seats
            right = 6 in seats or 7 in seats or 8 in seats or 9 in seats
            middle = 4 in seats or 5 in seats or 6 in seats or 7 in seats

            if not left and not right:
                families += 2
            elif not left or not right:
                families += 1
            elif not middle:
                families += 1

        families += 2 * (n - len(res_seats))

        return families

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    n = 3
    reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    print("Test Case 1:", solution.maxNumberOfFamilies(n, reservedSeats))  # Output: 4

    # Test Case 2
    n = 2
    reservedSeats = [[2,1],[1,8],[2,6]]
    print("Test Case 2:", solution.maxNumberOfFamilies(n, reservedSeats))  # Output: 2

    # Test Case 3
    n = 4
    reservedSeats = []
    print("Test Case 3:", solution.maxNumberOfFamilies(n, reservedSeats))  # Output: 8

if __name__ == "__main__":
    main()
