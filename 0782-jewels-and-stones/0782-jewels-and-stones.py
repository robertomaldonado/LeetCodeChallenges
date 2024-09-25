class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = dict()
        count = 0
        
        for c in list(stones):
            stones_dict[c] = stones_dict.get(c,0) + 1  
            
        for j in list(jewels):
            count += stones_dict.get(j,0)
        
        return count
            
            