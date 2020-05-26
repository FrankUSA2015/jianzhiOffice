# -*- coding: utf-8 -*-
#因为是二叉排序树所以要先

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    head = None
    pre = None
    def dfs(self,root:'Node'):
        if not root:
            return root
        self.dfs(root.left)
        if self.pre:
            self.pre.right = root
            root.left = self.pre
        else:
            self.head=root
        self.pre = root
        self.dfs(root.right)
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root :
            return root
        self.dfs(root)
        self.pre.right=self.head
        self.head.left=self.pre
        return self.head