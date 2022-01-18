class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        k = s[0]
        ans = 0
        
        for i in range(len(s)):
            if s[i] in k:
                if len(k) > ans:
                    ans = len(k)
                k = k[k.index(s[i])+1:i]
            k += s[i]
        return max(ans, len(k))