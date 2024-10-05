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
            if item in pairings.keys():
                stack.append(item)
            else:
                if len(stack)==0:
                    return False

                prev_opening = stack.pop()
                if pairings[prev_opening] != item:
                    return False

        return len(stack)==0
