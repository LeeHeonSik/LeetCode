class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        M = {}
        
        def cnt(d,F):
            if (d,F) in M :
                return M[(d,F)]
            
            if d<0 or F <=0:
                return 0
            if F < d or F > d*f:
                return 0
            if F == d or (d==1 and f >= F):
                return 1
            
            ans = 0
            for i in range(1,f+1):
                ans += cnt(d-1,F-i)

            M[(d,F)] = ans
            return ans
        

        return cnt(d,target) % (10**9 +7)