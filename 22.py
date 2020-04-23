# -*- coding: utf-8 -*-
#本题注意要在第一次循环的时候就要记录每一个节点的位置，这里用字典记录，因为字典的查找使用hash
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i=0
        lnode = {}
        bb=head
        while bb:
            i=i+1
            lnode[i]=bb
            bb=bb.next
        n=i-k+1
        return lnode[n]
