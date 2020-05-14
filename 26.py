# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def resur(self,A: TreeNode, B: TreeNode):
        if not B:
            return True
        if not A or A.val!=B.val:
            return False
        return self.resur(A.left,B.left) and self.resur(A.right,B.right)
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool(A and B) and(self.resur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))
