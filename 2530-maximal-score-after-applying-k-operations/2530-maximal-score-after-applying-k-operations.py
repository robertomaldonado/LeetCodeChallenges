class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        max_heap = list()

        for num in nums:
            heapq.heappush(max_heap, -num)
        while k > 0:
            k-=1
            max_el = -heapq.heappop(max_heap)
            ans += max_el

            heapq.heappush(max_heap, -ceil(max_el / 3))
        return ans