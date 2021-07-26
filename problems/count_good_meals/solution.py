class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic={}
        k=[]
        for i in range(22):
            k.append(2**i)
        for i in range(len(deliciousness)):
            dic[deliciousness[i]]=dic.get(deliciousness[i],0)+1
        ans=0
        for i in range(len(deliciousness)):
            dic[deliciousness[i]]-=1
            for j in range(22):
                if k[j]-deliciousness[i]>=0:
                    a=k[j]-deliciousness[i]
                    ans+=dic.get(a,0)
        return ans%(10**9 +7)