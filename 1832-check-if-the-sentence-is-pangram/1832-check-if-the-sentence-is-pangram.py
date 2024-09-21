class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        reps = set()
        for letter in sentence:
            reps.add(letter)
        return len(reps) == 26
            