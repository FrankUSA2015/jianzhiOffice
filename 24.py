# -*- coding: utf-8 -*-
#本题的难点是先要扫描一遍链表，把链表的值放到字典中，然后再从字典中取数，创建反向链表。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        i = 0
        lnode = {}
        bb = head
        cc=None
        ff=None
        while bb:
            i = i + 1
            lnode[i] = bb.val
            bb = bb.next
        for data in range(i):
            n=i-data
            if n==i:
                cc=ListNode(lnode[n])
                ff =cc
            else:
                bb=ListNode(lnode[n])
                cc.next=bb
                cc=bb
        return ff
