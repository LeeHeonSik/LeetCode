class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ans = ""
        if l1 > l2 :
            for i in range(l2):
                ans += word1[i]
                ans += word2[i]
            ans += word1[l2::]
        else:
            for i in range(l1):
                ans += word1[i]
                ans += word2[i]
            ans += word2[l1::]
        return ans