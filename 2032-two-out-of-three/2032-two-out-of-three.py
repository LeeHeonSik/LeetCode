class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        ans = []
        for i in s1:
            if i in s2 or i in s3:
                ans.append(i)
        for j in s2:
            if j in s1 or j in s3:
                if j not in ans:
                    ans.append(j)
        return ans