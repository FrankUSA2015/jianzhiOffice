# -*- coding: utf-8 -*-
#这个题计算了一遍上三角，计算了一遍下三角。这样时间复杂度大大下降。
class Solution:
    def constructArr(self, a):
       res=[]
       temp=1
       b=[1 for _ in range(len(a))]
       for i in range(1,len(a)):
           b[i]=b[i-1]*a[i-1]
       for i in range(len(a)-2,-1,-1):
           temp*=a[i+1]
           b[i]*=temp
       return b
aa=[1,2,3,4,5]
bb=Solution()
print(bb.constructArr(aa))