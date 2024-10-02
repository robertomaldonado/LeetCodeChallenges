"""
Input: weight = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
700, 800, 800, 900, 950, 1000
1. 7 + 8 + 8 + 9 + 9.5 + 10 = 51.5 > 50
so I drop the max weight to increase my capacity
41.5 < 50
count all the sum of apples, and return items count
"""
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        max_cap = 5000
        while sum(weight) > max_cap:
            weight.pop(-1)
        return len(weight)
        