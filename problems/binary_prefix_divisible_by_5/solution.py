class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        k = ''
        for i in nums:
            k = k + str(i)
            if int(k,2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans