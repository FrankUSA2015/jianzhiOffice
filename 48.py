# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict ={}
        tmp=0#这里的tmp是用来存储上一个位的长度
        res =0#用于存储最长的长度。
        #加上tmp和res的目的是减少存储的占用空间，因为记录每一个j所对的字符的长度是需要空间的。
        for j in range(len(s)):
            i = str_dict.get(s[j],-1)
            str_dict[s[j]]=j
            tmp = tmp+1 if j-i>tmp else j-i
            res =max(res,tmp)
        return res