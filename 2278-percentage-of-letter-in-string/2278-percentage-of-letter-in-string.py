class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        k = s.count(letter)
        return int(100 * (k/len(s)))