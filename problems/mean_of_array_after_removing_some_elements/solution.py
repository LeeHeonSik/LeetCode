class Solution:
    def trimMean(self, arr: List[int]) -> float:
        k = len(arr) // 20
        arr.sort()
        l = arr[k:-k]
        return sum(l)/len(l)
        # return round((sum(l) / l),6)
        
        