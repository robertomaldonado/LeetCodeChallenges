class Solution:
    def reverseString(self, s: List[str]) -> None:
        right = 0
        left = len(s)-1
        while left > right: 
            s[left], s[right] = s[right], s[left]
            left -=1 
            right +=1
        