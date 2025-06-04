# Problem: Min Stack
# Link: https://leetcode.com/problems/min-stack/description/
# Difficulty: Medium
# Time complexity: O(1) for all operations
# Space complexity: O(n)

# Solution: Maintain two stacks — one for the actual values and one for tracking the current minimum.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Test cases
def main():
    min_stack = MinStack()
    
    # Test Case 1
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("Test Case 1 - getMin:", min_stack.getMin())  # Output: -3
    min_stack.pop()
    print("Test Case 1 - top:", min_stack.top())        # Output: 0
    print("Test Case 1 - getMin:", min_stack.getMin())  # Output: -2

    # Test Case 2
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(0)
    print("Test Case 2 - getMin:", min_stack.getMin())  # Output: 0
    min_stack.pop()
    print("Test Case 2 - getMin:", min_stack.getMin())  # Output: 1

if __name__ == "__main__":
    main()
