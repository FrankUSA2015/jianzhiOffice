# -*- coding: utf-8 -*-
class Solution:
    def search(self, nums, target: int) -> int:
        sum_num=0
        for data in nums:
            if data==target:
                sum_num+=1
            if data>target:
                break
        return sum_num
aa = Solution()
nums = [5,7,7,8,8,10]
print(aa.search(nums,6))