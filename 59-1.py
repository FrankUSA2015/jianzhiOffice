# -*- coding: utf-8 -*-
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        max_list=[]
        temp=[]
        for data in nums:
            if len(temp)<k:
                temp.append(data)
            elif len(temp)==k:
                max_list.append(max(temp))
                del temp[0]
                temp.append(data)
        if len(temp)==k:
            max_list.append(max(temp))
        return max_list
aa= Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(aa.maxSlidingWindow(nums,k))