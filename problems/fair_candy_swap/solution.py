class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        d = sum(aliceSizes) - sum(bobSizes)
        d = d//2
        for i in aliceSizes:
            if (i-d) in set(bobSizes):
                return [i,i-d]