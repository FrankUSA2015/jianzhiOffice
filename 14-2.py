# -*- coding: utf-8 -*-
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            return (n-1)%1000000007
        a=round(n/3)
        b = n%3
        if b ==0:
            return int(3**a)%1000000007
        if b==1:
            return int(3**a-1*4)%1000000007
        return int(3**a*2)%1000000007