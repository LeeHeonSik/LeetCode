class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        odd = "aceg"
        even = "bdfh"
        n = int(coordinates[1]) % 2
        if n == 1 :
            if coordinates[0] in odd :
                return False
            else:
                return True
        if n == 0 :
            if coordinates[0] in even :
                return False
            else:
                return True