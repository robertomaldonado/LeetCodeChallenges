class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = list()   
        for point in points:
            x = point[0]
            y = point[1]
            dist_to_org = sqrt(x**2 + y **2)
            # Add to heap the distance to origin and the point
            heapq.heappush(heap, (dist_to_org, point))
        # Extract the lower k
        ans = list()
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans