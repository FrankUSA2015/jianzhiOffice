# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        res = []
        path = []

        def recur( root: TreeNode, sum: int):
            if not root:
                return
            path.append(root.val)
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, sum)
            recur(root.right, sum)
            path.pop()

        recur(root,sum)
        return res