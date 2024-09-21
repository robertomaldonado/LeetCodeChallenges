class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        ans = 0
        for i in arr:
            if i + 1 in arr:
                ans += 1
            
        return ans
            
            
        
        
        