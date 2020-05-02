# -*- coding: utf-8 -*-
#本题用到了滑动窗口的方法来解决这道题目。
#注意这个求和的数组的末尾数就是target。1,2,3，.....target
class Solution:
    def findContinuousSequence(self, target: int):
        i=1
        j=1
        res =[]
        sum=0
        while i<=target/2:
            if sum<target:
                sum=sum+j#注意要先加j再做j的加法。
                j = j + 1
            elif sum>target:
                sum=sum-i
                i = i + 1
            elif sum==target:
                temp=list(range(i,j))
                res.append(temp)
                sum=sum-i
                i = i + 1
        return res

aa= Solution()
tat = 3
print(aa.findContinuousSequence(tat))