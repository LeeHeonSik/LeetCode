class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flipping(row):
            row = row[::-1]
            return row
        
        def inverting(row):
            for i in range(len(row)):
                row[i] = 1 - row[i]
            return row
        
        for i in range(len(image)):
            image[i] = flipping(image[i])
            image[i] = inverting(image[i])
        return image