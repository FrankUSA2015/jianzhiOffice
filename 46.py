# -*- coding: utf-8 -*-
#这个题目是一道动态规划问题
class Solution:
    def translateNum(self, num: int) -> int:
        ss = str(num)
        a = 1
        b = 1
        for i in range(2,len(ss)+1):#最后循环取len(ss)+1是因为ss[i-2:i]这个字符串取不到右侧的值，只能取到i-2,i-1不能取到i
            tmp = ss[i-2:i]
            c = a+b if "10"<=tmp<="25" else a
            b = a
            a = c
        return a