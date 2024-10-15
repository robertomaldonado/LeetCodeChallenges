"""
Input: s = "100". => "001"
Output: 2
Explanation: We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "010".
- Swap s[1] and s[2], s = "001".
It can be proven that the minimum number of steps needed is 2.
Algorithm: 
100 so we get the index of the first 0 we find, this is i=0
we expect 0 0's after i=0, so for each 0 we add a one.
i=2
101 i=, i=1
find 0's after 1's
01010 
00110
00101
00011
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        white_position = 0
        total_swaps = 0

        # Iterate through each ball in the string
        for current_pos, char in enumerate(s):
            if char == "0":
                # Calculate the number of swaps needed
                total_swaps += current_pos - white_position

                # Move the next available position for a white ball one step to the right
                white_position += 1

        return total_swaps
        