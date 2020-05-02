# -*- coding: utf-8 -*-
#本题利用了双指针的方法
class Solution:
   def twoSum(self, nums, target: int):
       i = 0
       j = len(nums)-1
       res = []
       while i < j:
           sum_num = nums[i] + nums[j]
           if sum_num > target:
               j = j - 1
           elif sum_num < target:
               i = i + 1
           else:
               temp = [nums[i], nums[j]]
               res.append(temp)
               i=i+1 #注意找到后也要移动
       return res[0]


