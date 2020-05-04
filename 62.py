# -*- coding: utf-8 -*-
#约瑟夫环问题
#这个题目用到了递归的方法
import sys
sys.setrecursionlimit(100000)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def f(n,m):
            if n==0:
                return 0
            x= f(n-1,m)
            return (x+m)%n
        return f(n, m)

aa = Solution()
print(aa.lastRemaining(5,3))