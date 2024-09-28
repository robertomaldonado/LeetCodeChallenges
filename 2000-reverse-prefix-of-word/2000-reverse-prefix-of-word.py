"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
Ex 1.
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
no letter, return word
[a, b, c, d, e, f] i=0, limit=0, ch= d
 ^
 Now we have:
[a, b, c, d, e, f] i=3, limit=0
          ^
1. seek for index
we can trim end inclusive and keep tail, then reverse, add tail, join
and return
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        wrd = list(word)
        limit = 0
        if ch not in wrd:
            return word
        for i in range(len(word)):
            if word[i] == ch:
                limit = i
                break
        tail = wrd[i+1:]
        head = wrd[:i+1]

        i = 0
        while i < len(head):
            tail.insert(0, head[i])
            i+=1

        return "".join(tail)
