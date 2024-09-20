"""
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
----------
Input: nums = [1,-2,-3]
Output: 5
[1,-1,-4] => 1 = x - 4 => 0 = x - 5 => x = -(-4) + 1
Input: nums = [1,2]
Output: 1
[1,3] => -(1) + 1 = 0 if 0 => 1
Input: nums = [0, 1,2,1,3]
Output: 1
[0,1,3,4,7] => 0 +1 = 1
----------
Having the a sums array, may help:
[-3, -1, -4, 0, 2] should be the minimum + 1 if negative. If min is 0 return 1
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
#       Create sums list
        sums = [nums[0]]
        for i in range(1,len(nums)):
            sums.append(nums[i] + sums[-1])
        if min(sums) < 0:
            return abs(min(sums)) + 1
        return 1
