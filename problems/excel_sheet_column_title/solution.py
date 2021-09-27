class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=''
        
        while columnNumber:
            columnNumber -= 1
            ans = chr(65+(columnNumber % 26)) + ans
            columnNumber = columnNumber // 26
        return ans
            