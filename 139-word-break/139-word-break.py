class Solution:
    def dp(self, s, wordDict, memo):
        if s in memo:
            return memo[s];
        if s == "":
            return True;

        for i in wordDict:
            if s.find(i) == 0:
                memo[s] = self.dp(s[len(i)::], wordDict, memo);
                if memo[s] == True:
                    return True;

        memo[s] = False;
        return memo[s];

    def wordBreak(self, s, wordDict):
        return self.dp(s, wordDict, {});