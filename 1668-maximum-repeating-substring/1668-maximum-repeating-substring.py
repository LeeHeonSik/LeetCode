class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        if word not in sequence:
            return ans

        n = len(word)
        for i in range(1, len(sequence)//n + 1):
            if word * i in sequence:
                ans = i
        return ans