class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i] == '#':
                del ans[-1]
                del ans[-1]
                ans.append(chr(int(s[i-2:i])+96))
            else:
                ans.append(chr(int(s[i]) + 96))
        return (''.join(ans))
            
# 97 - a
# def change_alph(s):
    
#     for i in range(1, 10):
#         'ord(i + 96)' = i
        

#     for p in range(10, 27):
#         'ord(p + 96)' = i 
    
#     i