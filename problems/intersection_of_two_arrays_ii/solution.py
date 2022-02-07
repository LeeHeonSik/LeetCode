class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        ans = []
        for i, j in dic1.items():
            if i in dic2.keys():
                ans.extend([i]*min(dic1[i],dic2[i]))
        return ans