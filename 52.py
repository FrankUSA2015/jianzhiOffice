# -*- coding: utf-8 -*-
#用到了双指针法：
#因为node1和node2都是以同样的速度走同样的路所以最后如果有相同的节点一定会相遇的。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        while node1!=node2:
            if node1:
                node1=node1.next
            else:
                node1 =headB
            if node2:
                node2=node2.next
            else:
                node2=headA
        return node1