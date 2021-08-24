class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        S = sorted(score)
        S.reverse()
        grade = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(S) + 1)))
        
        for i in range(len(S)):
            score[score.index(S[i])] = grade[i]
        return score