# -*- coding: utf-8 -*-
#这个利用右上角的条件试验一下，
class Solution:
    def findNumberIn2DArray(self, matrix, target) -> bool:
         if len(matrix) == 0 or len(matrix[0]) == 0:
             return False
         i = 0
         j = len(matrix[0]) - 1
         while i<len(matrix) and j>=0:
             if matrix[i][j]==target:
                 return True
             elif matrix[i][j]>target:
                 # print(matrix[i][j])
                 j=j-1
             elif matrix[i][j]<target:
                 # print(matrix[i][j])
                 i=i+1
         return False

aa = Solution()
bb = []
print(aa.findNumberIn2DArray(bb,3))