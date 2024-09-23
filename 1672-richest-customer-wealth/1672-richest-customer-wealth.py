class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for customer in accounts:
            ans = max(ans, sum(customer))
        return ans