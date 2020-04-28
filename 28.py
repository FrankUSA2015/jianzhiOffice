# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l,r):
            if not l and not r:
                return True
            if not l or not r or r.val!=l.val:
                return False
            return recur(l.right,r.left) and recur(l.left,r.right)

        if root:
            return recur(root.left,root.right)
        else:
            return True