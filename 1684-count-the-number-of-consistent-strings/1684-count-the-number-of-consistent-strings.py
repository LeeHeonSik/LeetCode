class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            if all(j in allowed for j in words[i]):
                ans += 1
        return ans