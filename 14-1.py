# -*- coding: utf-8 -*-
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3 :
            return n-1
        a=n//3
        b=n%3
        if b==0:
            return int(math.pow(3,a))
        if b==1:
            return int(math.pow(3,a-1)*4)
        return int(math.pow(3,a)*2)