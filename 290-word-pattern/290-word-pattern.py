class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return [pattern.index(i) for i in pattern] == [s.split(" ").index(i) for i in s.split(" ")]