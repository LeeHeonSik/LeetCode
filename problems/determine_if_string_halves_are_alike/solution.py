class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        e = len(s)//2
        s1 = s[:e]
        s2 = s[e:]
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c1, c2 = 0, 0
        for i in v:
            if i in s1:
                c1 += s1.count(i)
            if i in s2:
                c2 += s2.count(i)
        return c1 == c2