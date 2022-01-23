class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 1
        for i in sentences:
            k = i.split()
            ans = max(ans,len(k))
        
        return ans