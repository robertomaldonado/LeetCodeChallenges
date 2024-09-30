"""
[3,2,2,1] => [1,2,2,3]
Greedy approach:
Link a heavy person with the lightest, if not then no other can be with them
Sort
ptr left, right
add left + right if exceeds => decrease right, increase countger by one
return counter
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        boat_count , left = 0, 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
            right -= 1
            boat_count +=1
        return boat_count
