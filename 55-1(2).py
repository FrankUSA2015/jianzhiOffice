# -*- coding: utf-8 -*-
#深度优先搜索里的，前序遍历。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1