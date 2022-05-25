class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        k = ord(target)
        for let in letters:
            if ord(let) > k:
                return let
        return letters[0]