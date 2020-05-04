# -*- coding: utf-8 -*-
#本题用到了动态规划的思想。
class Solution:
    def twoSum(self, n: int):
        res=[]
        dp=[[0 for _ in range(n*6+1)] for _ in range(n+1)]#这样多出第0行和第0列
        for i in range(1,7):
            dp[1][i]=1
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    if j-k>=1 and dp[i-1][j-k]>0:
                        dp[i][j]+=dp[i-1][j-k]
        for i in range(1,n*6+1):
            if dp[n][i]>0:
                res.append(dp[n][i]/(6**n))
        return res
