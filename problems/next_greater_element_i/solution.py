class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            k = nums2.index(i)
            if k == len(nums2) -1 :
                ans.append(-1)
                continue
            if max(nums2[k::]) <= i:
                ans.append(-1)
                continue
            for j in nums2[k::]:
                if j > i:
                    ans.append(j)
                    break
             
        return ans