class Solution:
    def digitCount(self, num: str) -> bool:
        dic = collections.Counter(num)
        for i in range(len(num)):
            if num[i] != str(dic[str(i)]):
                return False
        return True