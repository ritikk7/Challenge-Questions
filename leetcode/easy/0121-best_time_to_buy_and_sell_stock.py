# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(1)

# Solution: Track the minimum price seen so far and compute the maximum profit at each step.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    prices = [7,1,5,3,6,4]
    print("Test Case 1:", solution.maxProfit(prices))  # Output: 5

    # Test Case 2
    prices = [7,6,4,3,1]
    print("Test Case 2:", solution.maxProfit(prices))  # Output: 0

    # Test Case 3
    prices = [2,4,1]
    print("Test Case 3:", solution.maxProfit(prices))  # Output: 2

if __name__ == "__main__":
    main()
