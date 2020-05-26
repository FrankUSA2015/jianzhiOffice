# -*- coding: utf-8 -*-
#复制复杂链表的方法

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def get_node(node:'Node'):
            if not node:
                return node
            if node in visited:
                return visited[node]
            else:
                new_no = Node(node.val,None,None)
                visited[node]=new_no
                return visited[node]


        if not head:
            return head
        old_node = head
        new_node = Node(head.val,None,None)
        visited[old_node]=new_node
        while old_node:
            new_node.next=get_node(old_node.next)
            new_node.random = get_node(old_node.random)
            old_node=old_node.next
            new_node=new_node.next
        return visited[head]