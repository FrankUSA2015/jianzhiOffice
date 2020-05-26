# -*- coding: utf-8 -*-
#排序的规则发生了变化就是
#if xy>yx: x>y
#else x<y
class Solution:
    def minNumber(self, nums: [int]) -> str:
        data = [str(num) for num in nums]
        data_size = len(data)
        def quick(left:int,right:int):
            if left>=right:
                return
            lf_index = left+1
            while data[lf_index]+data[left] < data[left]+data[lf_index]:
                if lf_index >= data_size-1:
                    break
                lf_index += 1
            rg_index = right
            while data[rg_index]+data[left]>data[left]+data[rg_index]:
                rg_index-=1
            while lf_index<rg_index:
                data[lf_index],data[rg_index]=data[rg_index],data[lf_index]
                lf_index+=1
                while data[lf_index] + data[left] < data[left] + data[lf_index]:
                    lf_index += 1
                rg_index-=1
                while data[rg_index] + data[left] > data[left] + data[rg_index]:
                    rg_index -= 1
            data[left],data[rg_index]=data[rg_index],data[left]
            quick(left,rg_index-1)
            quick(rg_index+1,right)

        quick(0,len(data)-1)
        return ''.join(data)
aa = Solution()
bb=[1,2,4,8,16,32,64,128,256,512]
print(aa.minNumber(bb))