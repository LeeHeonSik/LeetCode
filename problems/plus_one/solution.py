class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        if len(digits)==1 and digits[0] != 10:
            return digits
        for i in range(1,len(digits)):
            if digits[-i] == 10:
                digits[-i]=0
                digits[-i-1]+=1
            else:
                return digits
        if digits[0] == 10 and sum(digits)==10:
            digits.append(0)
            digits[0]=1
            return digits
        else:
            return digits