class Solution:
    def reformatDate(self, date: str) -> str:
        dic_m = {"Jan" : '01', "Feb" : '02', "Mar" : '03', "Apr" : '04', "May" : '05', "Jun" : '06', "Jul" : '07', "Aug" : '08', "Sep" : '09', "Oct" : '10', "Nov" : '11', "Dec" : '12'}
        data = date.split()
        if len(data[0]) == 3:
            data[0] = '0' + data[0][0]
        else:
            data[0] = data[0][:2]
        ans = data[2] + '-' + dic_m[data[1]] + '-' + data[0]
        return ans