class Solution:
    def makeFancyString(self, s: str) -> str:
        s=list(s)
        if len(s) < 3:
            return "".join(s)
        elif len(s)>=3:
            ans=s[0]
            count=1
            for i in range(1,len(s)):
                c=s[i]
                if c == s[i-1] :
                    count+=1
                    if count<3:
                        ans+=c
                    else:
                        continue
                else:
                    ans+=c
                    count=1
        return ans