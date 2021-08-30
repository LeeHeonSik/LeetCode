class Solution:
    def maxProfit(self, ivt: List[int], order: int) -> int:
        ivt = sorted(ivt, reverse = True)
        ivt.append(0)
        ans = 0
        c = 1
        for i in range(len(ivt)-1): 
            if ivt[i] > ivt[i+1]: 
                if c * (ivt[i] - ivt[i+1]) < order: 
                    ans += c * (ivt[i] + ivt[i+1] + 1)*(ivt[i] - ivt[i+1])//2
                    order -= c * (ivt[i] - ivt[i+1])
                else: 
                    Q = order // c
                    R = order % c
                    ans += (c * (2*ivt[i] - Q + 1) * Q//2) + R*(ivt[i] - Q)
                    return ans % (10**9 + 7)
            c += 1