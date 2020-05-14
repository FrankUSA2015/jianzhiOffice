# -*- coding: utf-8 -*-
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
       visit =set()
       def dfs(i,j,si,sj):
           if i>=m or j>=n or k<(si+sj) or (i,j) in visit:
               return 0
           visit.add((i,j))
           return 1+ dfs(i+1,j,si+1 if (i+1)%10!=0 else si-8 ,sj)+dfs(i,j+1,si,sj+1 if (j+1)%10!=0 else sj-8)
       return dfs(0,0,0,0)
