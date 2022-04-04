class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = collections.Counter(nums1)
        dic2 = collections.Counter(nums2)
        ans = []
        if len(nums1) >= len(nums2):
            for i in dic2.keys():
                if i in dic1.keys():
                    ans.append(i)
        else:
            for i in dic1.keys():
                if i in dic2.keys():
                    ans.append(i)
        return ans