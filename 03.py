# -*- coding: utf-8 -*-
class Solution:
    def findRepeatNumber(self, nums) -> int:
        first_num = []
        for data in nums:
            if data not in first_num:
                first_num.append(data)
            else:
                return data
aa = Solution()
bb= [2, 3, 1, 0, 2, 5, 3]
print(aa.findRepeatNumber(bb))