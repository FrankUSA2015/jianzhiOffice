# -*- coding: utf-8 -*-
class Solution:
    def permutation(self, s: str) -> [str]:
        cc=list(s)
        res = []
        def dfs(x):
            if x==len(cc)-1:
                res.append(''.join(cc))
                return
            dic = set()
            for i in range(x,len(cc)):
                if cc[i] in dic:
                    continue
                dic.add(cc[i])
                cc[i],cc[x] = cc[x],cc[i]#对x位置和i的位置进行交换
                dfs(x+1)
                cc[i],cc[x] = cc[x], cc[i]#对x位置和i的位置进行交换
        dfs(0)
        return res