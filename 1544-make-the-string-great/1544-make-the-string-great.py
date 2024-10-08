"""
Input: s = "abBAcC"
Output: ""
Algorithm:
--------------
|ab
--------------
see B, pop b
--------------
|a
--------------
see A, pop a
--------------
|c
--------------
see C, pop c

"""
class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        for curr_char in list(s):
            
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        
        return "".join(stack)