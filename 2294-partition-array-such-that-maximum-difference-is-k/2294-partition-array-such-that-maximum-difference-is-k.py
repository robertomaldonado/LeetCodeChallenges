"""
Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.

In this case I can sort, it would be the equivalent
[1,2,3,5,6]
define ans, and placeholder for value
now starting fron last = 1, index 0 => num[1] - last < k: then add to ans, move last to be the curr
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        count = 1 #There is always a subset
        sorted_nums = sorted(nums)
        past_value = sorted_nums[0]

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - past_value > k:
                past_value = sorted_nums[i]
                count+=1

        return count