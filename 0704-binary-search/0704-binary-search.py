"""
[1,2,3,4,5,6,7,8,9] nums
 ^       ^       ^
 0       4       8
 l       m       r

target = 7 
if nums[4] > target, 9 > 7?:

[1,2,3,4,5,6,7,8,9] nums
         ^   ^   ^
         4       8
         l       r
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and nums[0] == target:
            return 0
        left = 0
        right = len(nums)-1

        while right > left:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: #move to the right
                left = mid + 1
            else: #move to the left
                right = mid - 1
        return -1