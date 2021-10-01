class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = 2000
        ans=[]
        for i in list2:
            if i in list1:
                d = list1.index(i) + list2.index(i)
                if m == d:
                    ans.append(i)
                elif m > d:
                    ans.clear()
                    m = d
                    ans.append(i)
        return ans