# -*- coding: utf-8 -*-
#这个题用到的方法是分别按照四个边的情况进行处理
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        left =  0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        res =[]
        while True:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top = top+1
            if top>bottom:
                break
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right=right-1
            if right<left:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom = bottom-1
            if bottom<top:
                break
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left =left +1
            if left>right:
                break
        return res