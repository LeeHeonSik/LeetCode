class Solution:
    def longestWord(self, words: List[str]) -> str:
        a=0
        b=""
        for i in words : 
            if a < len(i) or a == len(i) and b > i :
                c=0
                for j in range(len(i)):
                    if i[:j] in words:
                        c+=1
                if c == len(i) -1:
                    a=len(i)
                    b=i

        return b