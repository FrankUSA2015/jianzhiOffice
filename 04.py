# -*- coding: utf-8 -*-
#利用的矩阵特有的性质，本题的解题方法是利用矩阵的性质，输入矩阵的从左到右是增加的，从上往下是增加的。利用的是左下角这个条件。
#这个题目应该注意如果输入的为空list的情况，尤其是这样的情况[[]],这个在用len([[]]),表示的长度为1，而不是0
#第二在while循环里j应该小于的是matrix[0]而不是matrix，理由同上
class Solution:
    def findNumberIn2DArray(self, matrix, target) -> bool:
        i = len(matrix)-1
        j = 0
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j] ==target:
                return True
            elif matrix[i][j]>target:
                i=i-1
            elif matrix[i][j]<target:
                j=j+1
        return False
aa = Solution()
bb =[

]
print(aa.findNumberIn2DArray(bb,20))
