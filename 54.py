# -*- coding: utf-8 -*-
#解这道题利用了二叉排序树中序遍历可以得到一个从小到大的有序数组的性质。
#利用中序遍历的倒序的方法得到一个从大到小的有序数组。从而找到第k个
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        def dfs(root):
            if not root :
                return
            dfs(root.right)
            if self.k==0:
                return
            self.k -=1
            if self.k==0:
                self.res=root.val
            dfs(root.left)

        dfs(root)
        return self.res