# -*- coding: utf-8 -*-
class Solution:
    def printNumbers(self, n: int):
        num =10**n
        num_list =[]
        for data in range(1,num):
            num_list.append(data)
        return num_list

aa = Solution()
nn=3
print(aa.printNumbers(nn))