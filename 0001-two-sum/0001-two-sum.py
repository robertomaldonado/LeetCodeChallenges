"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in complements:
                return[i, complements[complement]]
            complements[num] = i

        return [-1, -1]
        



        