"""
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, curr = 0,0
        total = 0

        for i in range(k):
            total += nums[i]
        ans = total
        
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            ans = max(ans, total)
        return ans/k
            
            