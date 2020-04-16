# -*- coding: utf-8 -*-
#在deleteHead中注意判断A，B的顺序，不要反了，反了就会出错！
class CQueue:
    def __init__(self):
        self.A=[]#这个作为插入队列
        self.B=[]#作为把A中元素倒转到B的队列
        pass

    def appendTail(self, value: int) -> None:
        self.A.append(value)
        pass

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1

        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
        pass
