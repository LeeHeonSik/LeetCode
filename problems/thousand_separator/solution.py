class Solution:
    def thousandSeparator(self, n: int) -> str:
        return '.'.join([str(n)[::-1][i:i+3][::-1] for i in range(0, len(str(n)), 3)][::-1])