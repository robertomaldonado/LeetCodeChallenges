"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        curr_len = len(nums)
        while i < curr_len:
            if nums[i] == val: 
                nums.remove(nums[i])
                curr_len -= 1
            else:
                i +=1
                
        return len(nums)