class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coords = [0, 0]
        for move in moves:
            if move == "U":
                coords[0] += 1
            elif move == "D":
                coords[0] -= 1
            elif move == "R":
                coords[1] += 1
            else:
                coords[1] -= 1
        return coords[0] == 0 and coords[1] == 0
            