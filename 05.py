# -*- coding: utf-8 -*-
class Solution:
    def replaceSpace(self, s:str) -> str:
        dd = s.replace(" ","%20")
        return dd

aa = Solution()
bb = "We are happy."
print(aa.replaceSpace(bb))

