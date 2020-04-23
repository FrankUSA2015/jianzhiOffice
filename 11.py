# -*- coding: utf-8 -*-
class Solution:
    def minArray(self, numbers) -> int:
        max_num = numbers[0]
        min_num = numbers[0]
        for data in numbers:
            if max_num<=data:
                max_num=data
            else:
                return data
        if min_num<=max_num:
            return min_num

aa = Solution()
cc = [1,3,5]
print(aa.minArray(cc))