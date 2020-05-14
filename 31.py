# -*- coding: utf-8 -*-
class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        stack =[]
        i = 0
        for data in pushed:
            stack.append(data)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        return not stack