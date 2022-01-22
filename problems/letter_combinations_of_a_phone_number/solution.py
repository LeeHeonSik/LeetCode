from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dic = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7': 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        s = []
        for i in digits:
            s.append(dic[i])
        

        if len(s) == 1:
            return list(map(lambda x:"".join(x),set(product(s[0]))))
        elif len(s) == 2:
            return list(map(lambda x:"".join(x),set(product(s[0],s[1]))))
        elif len(s) == 3 :
            return list(map(lambda x:"".join(x),set(product(s[0],s[1],s[2]))))
        return list(map(lambda x:"".join(x),set(product(s[0],s[1],s[2],s[3]))))