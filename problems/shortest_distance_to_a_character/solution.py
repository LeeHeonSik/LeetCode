class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        C = []
        
        for i in range(len(s)):
            if s[i] == c:
                C.append(i)
                
        t, i, prev = 0, 0, 99999
        while i < len(s):

            if i > C[t]:
                prev = C[t]
                if t + 1 < len(C):
                    t += 1

            ans.append(min(abs(i - C[t]), abs(i - prev)))
            i += 1

        return ans