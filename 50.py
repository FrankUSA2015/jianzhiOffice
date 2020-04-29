# -*- coding: utf-8 -*-
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return ""
        s_dict = {}
        for i in range(len(s)):

          if s[i] in s_dict:
              s_dict[s[i]] =s_dict[s[i]]+1
          else:
              s_dict[s[i]] =1

        for key in s_dict:
            if s_dict[key]==1:
                return key

aa =Solution()
s = "abaccdeff"
print(aa.firstUniqChar(s))