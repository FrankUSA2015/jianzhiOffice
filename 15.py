# -*- coding: utf-8 -*-
#这个题用到了二进制运算的知识
#n&1=1 n的最右边一位为1
#n&1=0 n的最右边一位为0
#n >>= 1 ： 将二进制数字 nn 无符号右移一位
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res+=n&1#用来判断n的最右边一位是否为1
            n>>=1
        return res




aa =Solution()
bb = 0b00000000000000000000000000001011
print(aa.hammingWeight(bb))