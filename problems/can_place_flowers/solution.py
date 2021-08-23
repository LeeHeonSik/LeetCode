class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] ==0 :
                empty +=1
                flowerbed[i] = 1
        return empty >= n