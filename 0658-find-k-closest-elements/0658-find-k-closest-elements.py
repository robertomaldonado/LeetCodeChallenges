class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        max_heap = list()
        for num in arr:
            # Get the distance to number
            cur_dist = abs(x-num)
            # Add to heap a tuple, dist and number (negatives as we need a max heap)
            heapq.heappush(max_heap, (-cur_dist, -num))
            # If gone over, pop highest distance value
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Make the number positive again, pick the second elem of tuple
        # Sort the list comprehesion before returning it
        return sorted([-tup[1] for tup in max_heap])

