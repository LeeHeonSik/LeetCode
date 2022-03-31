class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code * 2
        for i in range(n):
            if k > 0:
                code[i] = sum(code[i+1:i+k+1])
            elif k < 0:
                code[i] = sum(code[n+i+k:n+i])
            elif k == 0:
                code = [0]*n
                return code
        return code[:n]