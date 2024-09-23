"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
Input: text = "nlaebolko"
Output: 1
Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.
b a l l o o n | a: 1, b: 1, l: 2, o: 2, n :1
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = [0,0,0,0,0]

        for c in text:
            if c == 'b': counts[0] += 1
            if c == 'a': counts[1] += 1
            if c == 'l': counts[2] += 1
            if c == 'o': counts[3] += 1
            if c == 'n': counts[4] += 1
        counts[3] = counts[3] //2
        counts[2]  = counts[2] //2

        return min(counts)
