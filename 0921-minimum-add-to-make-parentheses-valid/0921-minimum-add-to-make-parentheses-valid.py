"""
Input: s = "())"
Output: 1
so we do:
( insert to stack: stack = [(]
) remove from stack: stack = []
( add to stack: stack = [(]
I need whatever in stack moves
ex 2: (((
all in stack, i need 3 closers
"()))"
)) so => 2

))(( => 4


"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s: return 0
        stack = list()
        parenth = {"(": ")"}
        for c in s:
            if stack:
                if c == "(":
                    stack.append(c)
                elif c == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(c)
            else:
                stack.append(c)
        return len(stack)
        