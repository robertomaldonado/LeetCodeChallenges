"""
Input: s = "()[]{}"
Output: true
Ex 2.
Input: s = "(]"
Output: false
--------
Stack 
( [ ] )
     ^ 
|   |
|   |
|   |
----
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairings = {"(":")", "[":"]", "{":"}" }
                                           
        for item in s:
            if item in pairings.values() and len(stack) == 0:
                return False
            if item in pairings.keys():
                stack.append(item)
            if item in pairings.values():
                if  item == pairings[stack[-1]]:
                    stack.pop()
                else:
                    return False
            # print(stack)
        return len(stack) == 0

        return len(stack) == 0
            
