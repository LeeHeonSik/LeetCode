class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        
        for i in numbers:
            if numbers.count(target - i) == 1:
                ans.append(numbers.index(i)+1)
                ans.append(numbers.index(target - i)+1)
                return ans
            if numbers.count(target - i) == 2:
                ans.append(numbers.index(i)+1)
                numbers.remove(i)
                ans.append(numbers.index(i)+2)
                return ans
        if target == 0:
            ans.append(numbers.index(0)+1)
            numbers.remove(0)
            ans.append(numbers.index(0)+2)
            return ans