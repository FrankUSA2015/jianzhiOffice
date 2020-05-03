# -*- coding: utf-8 -*-
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
       sum_num =0
       ss=""
       for data in s:
           if sum_num<n:
               ss=ss+data
               sum_num+=1
           else:
               break
       bb=s.split(ss)[1]
       return bb+ss
aa=Solution()
bb="abcdefg"
print(aa.reverseLeftWords(bb,2))