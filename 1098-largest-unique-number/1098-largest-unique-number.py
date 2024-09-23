"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1
"""
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freqs = dict()
        uniques = list()
        for num in nums:
            freqs[num] = freqs.get(num,0) + 1
            
        for k, v in freqs.items():
            if v == 1:
                uniques.append(k)
        if len(uniques) > 0:
            return max(uniques)
        return -1