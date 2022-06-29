class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vow = 'aeiou'
        ans = 0
        
        for i in range(len(word)):
            for j in range(i+4, len(word)):
                dic = collections.Counter(word[i:j+1])
                if all(dic[v] >= 1 for v in vow) and len(dic) == 5:
                    ans += 1
        return ans