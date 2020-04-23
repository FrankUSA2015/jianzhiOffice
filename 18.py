# -*- coding: utf-8 -*-
# Definition for singly-linked list.
#这个链表的注意事项有两点
#1.如果要删除的数在链表的头部
#2.注意链表的下一个位置在判断数值时，要先判断这个是否为空。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head, val: int):
        if head.val==val:
            head=head.next
        bb = head
        while bb:
            # print(bb.val)
            cc = bb.next
            if cc:
                if cc.val == val:
                    bb.next=cc.next
            bb=bb.next
        return head
a1 = ListNode(4)
a2 = ListNode(5)
a3 = ListNode(1)
a4 = ListNode(9)
a1.next = a2
a2.next = a3
a3.next = a4
aa =Solution()
cc = aa.deleteNode(a1,4)