"""
Input: nums = [7, 4,  3,  9,  1,  8,  5,  2,  6  ], k = 3
        Sums: [7, 11, 14, 23, 24, 32, 37, 39, 45 ], k = 3
              |           |            | k+i = 3+3 = 6
              i-k       37 - 7 // 7 = 5
                           
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Ideas. 
The first index to have a value in the results is i=3 or i = k
We start with a prepopulated list [-1,-1,-1 ... ]
Begin looking for indexes and bounds
So if k = 3 then check we have data until i + k and i - k
then we get the sums to that point using the sums array:
    nums[i-k]  - sums[k - i] + sums [k+i]
Edge cases: 
k is 0, then averages are the same as nums

"""
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if k == 0:
            return nums
        ans = [-1 for x in range(len(nums))]
        if k > len(nums):
            return ans

#       Create a sums array
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        items = (2*k) +1
        
        start_index = k
        while start_index + k < len(nums):
            ans[start_index] = (sums[start_index+k] + nums[start_index-k] - sums[start_index-k]) // items
            start_index += 1
        return ans
        
        
        
        
        