class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        freqs = dict()
        for item in nums:
            freqs[item] = freqs.get(item,0) + 1

        ans = heapq.nlargest(k, freqs.keys(), key=freqs.get)
        return ans