class Solution:
    def maxScore(self, s: str) -> int:
        
        _max = 0
        for i in range(1,len(s)):
            m = s[:i].count('0') + s[i:].count('1')
            if m > _max :
                _max = m
        return _max