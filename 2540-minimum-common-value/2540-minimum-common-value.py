"""
We have to sorted arrays.
Pointer to nums1 and nums2, this is a double pointer problem
We iterate until we \have completed the length of both
Interrupt and return if both are equal.
Advance the opposite pointer if there is difference
[1,2,3]
 ^
[2,4]
 ^

[1,2,3]
   ^
[2,4]
 ^
"""
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_ptr, nums2_ptr = 0, 0
        ans = -1

        while nums1_ptr < len(nums1) and nums2_ptr < len(nums2):
            if nums1[nums1_ptr] == nums2[nums2_ptr]:
                return nums1[nums1_ptr]
            elif nums2[nums2_ptr] > nums1[nums1_ptr]:
                nums1_ptr+=1
            else:
                nums2_ptr += 1

        while nums1_ptr < len(nums1) and nums2_ptr+1 < len(nums2):
            if nums1[nums1_ptr] == nums2[nums2_ptr]:
                return nums1[nums1_ptr]
            elif nums2[nums2_ptr] > nums1[nums1_ptr]:
                nums1_ptr+=1
            else:
                nums2_ptr += 1

        while nums2_ptr < len(nums2) and nums1_ptr+1 < len(nums1):
            if nums1[nums1_ptr] == nums2[nums2_ptr]:
                return nums1[nums1_ptr]
            elif nums2[nums2_ptr] > nums1[nums1_ptr]:
                nums1_ptr+=1
            else:
                nums2_ptr += 1

        return ans
