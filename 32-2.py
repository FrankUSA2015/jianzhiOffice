# -*- coding: utf-8 -*-
#BFS广度优先算法的第二种表示方法
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:
            return []
        res =[]
        ques = collections.deque()
        ques.append(root)
        while ques:
            temp=[]
            for _ in range(len(ques)):#对于 python ，range() 的工作机制是在开启循环时建立一个列表，
                                      # 然后循环按照这个列表进行，因此“只会在进入循环前执行一次 len(queue) ”
                node = ques.popleft()
                temp.append(node.val)
                if node.left:
                    ques.append(node.left)
                if node.right:
                    ques.append(node.right)
            res.append(temp)
        return res