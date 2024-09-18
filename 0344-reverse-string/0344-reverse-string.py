class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        So we have: hello then we return olleh
        define pointers at 0 and len of s
        we swap, then advance. Consider that i,j cannot exceed each other
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        