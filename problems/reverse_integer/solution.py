class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            ans=int((str(x)[::-1]))
        elif x<0:
            ans=-1 * int((str(x*-1)[::-1]))
        elif x==0:
            ans=0
        elif x>=(2**31)-1 or x<=-2**31:
            ans=0
        if ans>=(2**31)-1 or ans<=-2**31:
            ans=0
        return ans