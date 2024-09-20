"""
Input: s = "Mr Ding"
Output: "rM gniD"
Do a list, with the given str. reverse string by string, then join then together ass str
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        ans = list()

        for word in s_list:
            w = [c for c in word]
            i, j = 0 , len(w)-1
            while i < j:
                w[i], w[j] = w[j], w[i]
                i+=1
                j-=1
            ans.append("".join(w))

        return " ".join(ans)