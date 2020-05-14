# -*- coding: utf-8 -*-
class Solution:
    postlist =[]
    def find_root(self,i, j):
        if i>=j:
            return True
        p = i
        while self.postlist[p]<self.postlist[j]:
            p+=1
        m=p
        while self.postlist[p]>self.postlist[j]:
            p+=1
        return p==j and self.find_root(i,m-1) and self.find_root(m,j-1)
    def verifyPostorder(self, postorder: [int]) -> bool:
        self.postlist = postorder
        return self.find_root(0,len(postorder)-1)