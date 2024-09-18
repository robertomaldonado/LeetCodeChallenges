"""
s = abc
t = ahbgdc
Using two pointer approach
a b c
      i
a h b g d c
          j
when done and i is len of s then it is a subsqe
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_t = len(t)
        len_s= len(s)
        while j < len_t and i < len_s:
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == len_s:
            return True
        return False