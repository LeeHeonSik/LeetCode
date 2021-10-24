class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for i in s:
            num += str(ord(i) - 96)
 
        for _ in range(k):
            num = sum([int(i) for i in str(num)])
            
        return num