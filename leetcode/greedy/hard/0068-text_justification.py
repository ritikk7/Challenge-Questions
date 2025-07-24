# Problem: Text Justification
# Link: https://leetcode.com/problems/text-justification/description/
# Difficulty: Hard
# Time complexity: O(n)
# Space complexity: O(n)

# Solution: Greedily add words to each line. Use even spacing between words and handle extra spaces. Special case for last line.

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def justify(line_words, line_len):
            spaces = maxWidth - line_len
            gaps = len(line_words) - 1 or 1
            space_div = spaces // gaps
            extra = spaces % gaps

            justified = ""
            for i, word in enumerate(line_words):
                justified += word
                if i < gaps:
                    justified += " " * (space_div + (1 if i < extra else 0))
            return justified

        output = []
        line_words = []
        line_len = 0

        for word in words:
            if line_len + len(word) + len(line_words) <= maxWidth:
                line_words.append(word)
                line_len += len(word)
            else:
                output.append(justify(line_words, line_len))
                line_words = [word]
                line_len = len(word)

        last_line = " ".join(line_words)
        last_line += " " * (maxWidth - len(last_line))
        output.append(last_line)

        return output

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print("Test Case 1:")
    for line in solution.fullJustify(words, maxWidth):
        print(f"'{line}'")

    # Test Case 2
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print("\nTest Case 2:")
    for line in solution.fullJustify(words, maxWidth):
        print(f"'{line}'")

    # Test Case 3
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    print("\nTest Case 3:")
    for line in solution.fullJustify(words, maxWidth):
        print(f"'{line}'")

if __name__ == "__main__":
    main()
