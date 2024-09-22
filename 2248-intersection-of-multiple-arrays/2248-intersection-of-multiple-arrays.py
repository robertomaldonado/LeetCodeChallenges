"""
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
"""
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 0: return []
        counts = dict()

        for sub_nums in nums:
            for num in sub_nums:
                counts[num] = counts.get(num, 0) + 1

        ans = []
        for i in range(1001):
            if counts.get(i) == len(nums):
                ans.append(i)
        return ans

        