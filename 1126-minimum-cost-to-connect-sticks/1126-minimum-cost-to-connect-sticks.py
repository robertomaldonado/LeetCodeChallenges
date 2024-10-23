class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            current_cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, current_cost)
            min_cost += current_cost
        return min_cost