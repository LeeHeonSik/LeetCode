class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(i.isupper() == True for i in word):
            return True
        if all(i.islower() ==True for i in word):
            return True
        if word[0].isupper() == True and all (i.islower() == True for i in word[1::]):
            return True
        return False