class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        L = list(text.split(' '))
        for i in L:
            if all(j not in i for j in brokenLetters):
                ans+=1
        return ans