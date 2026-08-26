class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for word in wordDict:
                length=len(word)
                if i>=length and dp[i-length] and s[i-length:i]==word:
                    dp[i]=True
                    break
        return dp[len(s)]
        