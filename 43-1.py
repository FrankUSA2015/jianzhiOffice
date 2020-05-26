# -*- coding: utf-8 -*-
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        lower =0
        high = n//10
        cur = n%10
        res =0
        while high!=0 or cur!=0:
            if cur==0:
                res+=digit*high
            elif cur==1:
                res+=digit*high+lower+1
            else:
                res+=(high+1)*digit
            lower += cur*digit
            cur = high%10
            high //=10
            digit *=10
        return res