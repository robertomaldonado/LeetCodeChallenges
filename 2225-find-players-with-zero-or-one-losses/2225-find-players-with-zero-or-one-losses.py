"""
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = dict()
        loosers = dict()
        winners_list = list()
        loosers_list = list()
        
        for i in range(len(matches)):
            winner = matches[i][0]
            looser = matches[i][1]
            winners[winner] = winners.get(winner ,0) + 1
            loosers[looser] = loosers.get(looser ,0) + 1
            
        for i in range(len(matches)):
            curr = matches[i][0]
            curr_2 = matches[i][1]
            
            if winners.get(curr ,0) > 0 and loosers.get(curr ,0) == 0 and curr not in winners_list:
                winners_list.append(curr)
            if loosers.get(curr_2 ,0) == 1:
                loosers_list.append(curr_2)
        return [sorted(winners_list), sorted(loosers_list) ]
        