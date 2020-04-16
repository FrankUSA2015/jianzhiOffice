# -*- coding: utf-8 -*-
# Definition for a binary tree node.
#这题目利用了递归的思想，最关键的地方有以下三点：
#1.找到根在中序遍历的位置，并且根据这个位置，找到他的左右子树
#2.在找左子树的根在前序遍历的位置的时候，根据前序遍历的性质，
    # 找到下一个节点就是前序遍历的根然后在确定左子树在中序遍历中的大体范围，
    # 一定是在上一棵树的左边开始，到上一棵树的根节点的在中序遍历的位置的前一个位置
#3.在找右子树的时候要注意他的根节点在前序遍历中的位置，这个位置等于现有的根节点的位置+中序遍历中左子树的长度+1
#注意右子树在中序遍历中的范围，他的右侧还是上一棵树的右侧，但是左侧等于上一棵树的根在中序遍历中的位置加一
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    dic ={}
    pre_order=[]
    def recur(self,pre_position,in_left,in_right):
        if in_left>in_right:
            return #这样返回的是null
        root = TreeNode(self.pre_order[pre_position])
        in_root = self.dic[self.pre_order[pre_position]]
        root.left = self.recur(pre_position+1,in_left,in_root-1)
        root.right =self.recur(pre_position+in_root-in_left+1,in_root+1,in_right)
        # print(self.pre_order[pre_position])
        return root
    def buildTree(self, preorder, inorder) -> TreeNode:
        self.pre_order=preorder
        for i ,data in enumerate(inorder):
            self.dic[data]=i
        return self.recur(0,0,len(inorder)-1)



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
aa = Solution()
aa.buildTree(preorder,inorder)