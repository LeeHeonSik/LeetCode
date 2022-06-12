from math import *
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        modulo = 10**9 + 7
        c = 0
        for i in range(1, n+1):
            if i in primes:
                c += 1
        
        ans = factorial(n-c) * factorial(c) % modulo
        return ans