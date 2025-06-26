# Problem: Simple Bank System
# Link: https://leetcode.com/problems/simple-bank-system/description/
# Difficulty: Medium
# Time complexity: O(1) for all operations
# Space complexity: O(n)

# Solution: Simulate bank operations with basic validation on account indexes and balances.

from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance) or self.balance[account1 - 1] < money:
            return False
        self.balance[account2 - 1] += money
        self.balance[account1 - 1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True

# Test cases
def main():
    bank = Bank([10, 20, 30, 40, 50])

    # Test Case 1
    print("Test Case 1 - transfer(1, 2, 5):", bank.transfer(1, 2, 5))  # Output: True
    print("Balances:", bank.balance)

    # Test Case 2
    print("Test Case 2 - withdraw(2, 50):", bank.withdraw(2, 50))  # Output: False
    print("Balances:", bank.balance)

    # Test Case 3
    print("Test Case 3 - deposit(3, 15):", bank.deposit(3, 15))  # Output: True
    print("Balances:", bank.balance)

if __name__ == "__main__":
    main()
