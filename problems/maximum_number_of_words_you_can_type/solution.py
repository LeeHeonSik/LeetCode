class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        L = list(map(str, text.split(' ')))
        ans = len(L)
        for i in range(len(L)):
            for j in brokenLetters:
                if j in L[i]:
                    ans -=1
                    break
        return ans
        