class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        s = list(s)
        for i in range(1,len(s)):
            if i % k == 0:
                s[-i] = '-' + s[-i]
        return (''.join(s)).upper()