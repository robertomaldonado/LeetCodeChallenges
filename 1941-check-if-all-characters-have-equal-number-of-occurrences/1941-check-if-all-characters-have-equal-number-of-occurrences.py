"""
Input: s = "abacbc"
Output: true
1 <= s.length <= 1000
{a:2, b:2, c:2}
{a:1, b:2, c:2}

s consists of lowercase English letters. so max we have 26 entries for the letter
"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freqs = dict()
        for c in s:
            freqs[c] = freqs.get(c,0) + 1
        k, one_freq = freqs.popitem()
        for k, v in freqs.items():
            if v != one_freq:
                return False
        return True