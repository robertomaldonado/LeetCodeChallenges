class Solution:
    def removeStars(self, s: str) -> str:
        len_list, s_list = len(s), list(s)
        i = 0
        while i < len_list:
            if s_list[i] == "*":
                del s_list[i-1:i+1]
                len_list-=2
                i-=2
            i+=1
        return "".join(s_list)