# -*- coding: utf-8 -*-
class Solution:
    def exchange(self, nums):
        odd =[]
        even =[]
        for data in nums:
            if data%2==0:
                even.append(data)
            else:
                odd.append(data)
        return odd+even
aa =Solution()
nums = [1,2,3,4]
print(aa.exchange(nums))