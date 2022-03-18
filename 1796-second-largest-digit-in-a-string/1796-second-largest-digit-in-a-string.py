class Solution:
    def secondHighest(self, s: str) -> int:
        ans = {}
        for i in range(len(s)):
            if s[i].isdigit():
                ans[s[i]] = ans.get(i,0) + 1
        if len(ans.keys()) <= 1:
            return -1
        else:
            ans = sorted(ans.items(),key=lambda x:x[0], reverse = True)
            return ans[1][0]