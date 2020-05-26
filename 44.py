# -*- coding: utf-8 -*-
class Solution:
    def findNthDigit(self, n: int) -> int:
        start,digit,count=1,1,9
        while n>count:#这里不能是等号，
            n-=count
            digit+=1
            start *=10
            count = 9*start*digit
        num = start+(n-1)//digit
        return int(str(num)[(n-1)%digit])
aa = Solution()
print(aa.findNthDigit(9))