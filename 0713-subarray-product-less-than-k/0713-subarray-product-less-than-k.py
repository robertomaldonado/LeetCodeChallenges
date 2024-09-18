"""
input: nums = [10,5,2,6], k=100
output: 8
Because we have:
 [10], [5],[2], [6],[10, 5], [5,2], [2,6], [5,2,6]
 
You can fix the right bound and then choose any value between left and right inclusive for the left bound. Therefore, the number of valid windows ending at index right is equal to the size of the window, which we know is right - left + 1
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, ans, curr = 0,0,1
        if k <= 1: return 0
        for right in range(len(nums)):
            curr = curr * nums[right]
            while curr >= k:
                curr = curr // nums[left]
                left += 1
            ans += right - left + 1 
        return ans 