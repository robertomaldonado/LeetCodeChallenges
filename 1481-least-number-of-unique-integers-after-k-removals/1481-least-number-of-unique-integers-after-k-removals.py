"""
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
Greedy approach:
count reps: {4: 1, 3:3, 2:1, 1:2}
reps.values.ordered: 
[3,2,1,1] k = 3
[3,2,1] k = 2
[3,2] k = 1 cant do 2, then return len od array
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = dict()
        for c in arr:
            freqs[c] = freqs.get(c ,0) + 1

        ordered_freqs = sorted(freqs.values(), reverse=True)
        while k:
            curr_f = ordered_freqs[-1]
            if curr_f <= k:
                k -= curr_f
                ordered_freqs.pop()
            else:
                break

        return len(ordered_freqs)