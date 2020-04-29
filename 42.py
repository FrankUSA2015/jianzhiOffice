# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums) -> int:
        dp=[]
        max_sum =nums[0]
        max_list =[]
        dp.append(nums[0])
        max_list.append(nums[0])
        for i in range(1,len(nums)):
            if (dp[i-1]+nums[i]>=max_sum and dp[i-1]+nums[i]>=nums[i]) or( dp[i-1]+nums[i]<max_sum and dp[i-1]+nums[i]>=nums[i]):
                tmp_sum = dp[i-1]+nums[i]
                dp.append(tmp_sum)
            else:
                tmp_sum = nums[i]
                dp.append(tmp_sum)
            if tmp_sum>=max_sum:
                max_sum = tmp_sum
        # print(dp)
        return max_sum

aa = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(aa.maxSubArray(nums))