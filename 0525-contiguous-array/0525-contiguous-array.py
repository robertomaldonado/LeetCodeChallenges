"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map1 = dict()
        map1[0] = -1
        max_len, count = 0, 0
        
        for i in range(len(nums)):
            tmp = 0
            if nums[i] == 1:
                tmp = 1
            else:
                tmp = -1
            count += tmp
            if count in map1.keys():
                max_len = max(max_len, i - map1.get(count))
            else:
                map1[count] = i
        return max_len
    