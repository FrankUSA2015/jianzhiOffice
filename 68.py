# -*- coding: utf-8 -*-
#这个题目是利用了二叉排序树的性质，因为二叉排序树是有序的，
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        while root:
            if root.val<p.val and root.val<q.val:
                root = root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else:
                break
        return root

