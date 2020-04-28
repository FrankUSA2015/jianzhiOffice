# -*- coding: utf-8 -*-
#BFS广度优先算法的遍历树的操作。
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res=[]
        ques = collections.deque()
        ques.append(root)
        while ques:
            node = ques.popleft()
            res.append(node.val)
            if node.left:
                ques.append(node.left)
            if node.right:
                ques.append(node.right)
        return res