# -*- coding: utf-8 -*-
class Solution:
    def majorityElement(self, nums) -> int:
        num_dict = {}
        list_num = len(nums)/2
        if len(nums)==1:
            return nums[0]
        for i in nums:
            if i in num_dict:
                num_dict[i]+=1
                if num_dict[i]>=list_num:
                    return i
            else:
                num_dict[i]=1
aa = Solution()
bb= [1,2,3,2,2,2,5,4,2]
print(aa.majorityElement(bb))