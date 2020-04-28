# -*- coding: utf-8 -*-
#第一种方法利用bfs
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res =0
        ques = collections.deque()
        ques.append(root)
        while ques:
            for _ in range(len(ques)):
                node = ques.popleft()
                if node.left:
                    ques.append(node.left)
                if node.right:
                    ques.append(node.right)
            res +=1
        return res