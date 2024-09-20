class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_as_list = list(s)
        i, j = 0, len(s_as_list)-1
        while i <= j:
            while not s_as_list[i].isalpha():
                if i + 1 <= len(s_as_list)-1:
                    i+=1
                else:
                    break
            while not s_as_list[j].isalpha():
                if j - 1 < 0:
                    i+=1
                else:
                    break
            s_as_list[j], s_as_list[i] = s_as_list[i], s_as_list[j]
            i+=1
            j-=1
        return "".join(s_as_list)
