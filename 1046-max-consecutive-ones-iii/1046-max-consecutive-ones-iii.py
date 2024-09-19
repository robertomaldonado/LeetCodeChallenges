"""
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # Reduce k only if encountered with a 0
            k -= 1 - nums[right]
            if k < 0:
                # If got rid of a 0, increase left and counter k
                k+= 1-nums[left]
                left += 1
        return right - left + 1