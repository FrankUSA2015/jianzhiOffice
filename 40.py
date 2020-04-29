# -*- coding: utf-8 -*-
class Solution:
    def getLeastNumbers(self, arr, k: int):
        arr.sort()
        res =[]
        for i in range(k):
            res.append(arr[i])
        return res