# -*- coding: utf-8 -*-
# Definition for singly-linked list.
#这个题目利用了list的反转函数。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head):
        vaild_num =[]
        aa= head
        while aa:
            vaild_num.append(aa.val)
            aa=aa.next
        vaild_num.reverse()
        return vaild_num

a1 = ListNode(1)
b1 = ListNode(3)
c1 = ListNode(2)

a1.next=b1
b1.next=c1
ss = Solution()
print(ss.reversePrint(a1))