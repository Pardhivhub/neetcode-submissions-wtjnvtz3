class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        memo={}
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            take_s1=False
            take_s2=False
            if i<len(s1) and s1[i]==s3[i+j]:
                take_s1=dfs(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                take_s2=dfs(i,j+1)
            memo[(i,j)]=take_s1 or take_s2
            return memo[(i,j)]
        return dfs(0,0)
            



        


        