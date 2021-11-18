class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = list(ransomNote)
        s2 = list(magazine)
        for i in s1:
            if i in s2:
                s2.remove(i)
            else:
                return False
        return True
                