"""
Counting + Two pointer
a b c a b c b b
^   ^
i   i+2 are included, in substr check for the set of str
if greater than the past, renew the value:
a b c a b c b b
  ^   ^
  i   i+2 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0 
        char_to_next_index = dict()

        i=0
        for j in range(n):
            if s[j] in char_to_next_index:
                i = max(char_to_next_index[s[j]], i)
            ans = max(ans, j-i+1)
            char_to_next_index[s[j]] = j+1
        return ans