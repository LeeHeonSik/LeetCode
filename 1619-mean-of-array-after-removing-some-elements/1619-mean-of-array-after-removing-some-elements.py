class Solution:
    def trimMean(self, arr: List[int]) -> float:
        k = len(arr) // 20
        for i in range(k):
            arr.remove(min(arr))
            arr.remove(max(arr))
            
        return round((sum(arr) / len(arr)),6)
        
        