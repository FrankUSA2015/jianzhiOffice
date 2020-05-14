# -*- coding: utf-8 -*-
#这个题的精妙所在有两点，第一点用双端队列的知识。第二点用了res来判断奇偶。
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        res = []
        dep = collections.deque([root])
        while dep:
            tmp = collections.deque()
            for _ in range(len(dep)):
                node = dep.popleft()
                if len(res)%2:#用res中的数量来判断这一层的奇偶，如果res可以整除则这一行就是偶数，否则这一行是奇数
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    dep.append(node.left)
                if node.right:
                    dep.append(node.right)
            res.append(list(tmp))
        return res