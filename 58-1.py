# -*- coding: utf-8 -*-
class Solution:
    def reverseWords(self, s: str) -> str:
        first=s.split()
        ss=''
        first.reverse()
        for key,data in enumerate(first):
            if key==0:
                ss=data
            else:
                ss=ss+" "+data

        return ss
aa = "  hello world!  "
bb=Solution()
print(bb.reverseWords(aa))