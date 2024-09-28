"""
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
 
Step 1
[0,1,0,3,12] i = 0
 ^
pop[i(=0)]
append(0)
              relocs=1, i=0
 Step 2
[1,0,3,12,0] i = 0
 ^
              relocs=1, i=1
[1,0,3,12,0] i = 0
   ^          relocs=1, i=1
[1,3,12,0,0] i = 0
   ^          relocs=2, i=1
[1,3,12,0,0] i = 0
     ^        relocs=2, i=2
[1,3,12,0,0] i = 0
        ^       relocs=2, i=3
[1,3,12,0,0] i = 0
          ^     relocs=2, i=4
[1,3,12,0,0] i = 0
            ^   relocs=2, i=5 => done
Custom example:       
[0,0,1] r=0, i=0
[0,1,0] r=1, i=0
[1,0,0] r=2, i=0
 ^
[1,0,0] r=2, i=1
   ^
[1,0,0] r=3, i=1
     ^
[1,0,0] r=4, i=1
     ^
Inspect, if 0 remove and move to the end. pop at index, append at end
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        relocations = 0
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            if relocations == nums_len:
                return i
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                relocations += 1
            else:
                i+=1
            