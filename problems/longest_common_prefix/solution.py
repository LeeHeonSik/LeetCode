class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        if len(strs)==0:
            return ans
        
        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                ans+=c
            else:
                break
        return ans