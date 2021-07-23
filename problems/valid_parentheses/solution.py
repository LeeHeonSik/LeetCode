class Solution:
    def isValid(self, s: str) -> bool:
        a=['(', '{', '[']
        b=[')', '}', ']']
        k=[]
        for i in s:
            if i in a:
                k.append(i)
            if i in b:
                if len(k)==0:
                    return False
                    break
                if a.index(k[-1]) == b.index(i):
                    k.pop()
                elif a.index(k[-1]) != b.index(i):
                    return False
                    break
        if len(k) != 0:
            return False
        else:
            return True