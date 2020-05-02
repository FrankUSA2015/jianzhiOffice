# -*- coding: utf-8 -*-
class Solution:
    def missingNumber(self, nums) -> int:
        if nums[0]!=0:
            return 0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]+1!=nums[i+1]:
                return nums[i]+1
        return len(nums)