# -*- coding: utf-8 -*-
#这个题目要注意大小王的存在，还有顺子的含义是
# 除了大小王以外最大值和最小值之间差值小于5
#而且除了大小王以外其他的数不能重复。
class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i]==0:
                joker+=1
            elif nums[i]==nums[i+1]:
                return False
        return nums[4]-nums[joker]<5
aa =Solution()
nums=[1,2,3,4,5]
print(aa.isStraight(nums))