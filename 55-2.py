# -*- coding: utf-8 -*-
#判断是不是平衡二叉树。
#这道题用到的是后续遍历+剪枝的方法来判断是否是平衡二叉树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def retroot(root):
            if not root:
                return 0
            left = retroot(root.left)
            if left==-1:
                return -1
            right = retroot(root.right)
            if right==-1:
                return -1
            return max(left,right)+1 if abs(left-right)<=1 else -1


        return retroot(root)!=-1
