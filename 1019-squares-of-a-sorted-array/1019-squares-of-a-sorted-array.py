"""
[-7,-3,2,3,11]
[49, 9]
[4,9,121]
[4,9,9,49,121]
"""
class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     i = 0
    #     neg_sq, pos_sq = list(), list()
    #     res =  list()
    #     while i < len(nums):
    #         if nums[i] < 0:
    #             neg_sq.append(nums[i]**2)
    #         else:
    #             pos_sq.append(nums[i]**2)
    #         i+=1
    #     j = len(neg_sq) -1
    #     i=0
        
    #     while i < len(pos_sq) and j >= 0:
    #         if pos_sq[i] < neg_sq[j]:
    #             res.append(pos_sq[i])
    #             i += 1
    #         else:
    #             res.append(neg_sq[j])
    #             j -=1 

    #     while j >= 0:
    #         res.append(neg_sq[j])
    #         j -= 1
                
    #     while i < len(pos_sq):
    #         res.append(pos_sq[i])
    #         i += 1
            
    #     return res
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = [0 for _ in range(len(nums))]
        pos = len(nums) - 1

        while left <= right: 
            current_right = nums[right]
            current_left = nums[left]
            if abs(current_right) > abs(current_left) : 
                ans[pos] = current_right**2
                right -= 1
            else:
                ans[pos] = current_left**2
                left += 1
            pos -= 1
        return ans


        