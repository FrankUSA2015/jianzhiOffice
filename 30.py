# -*- coding: utf-8 -*-
class MinStack:

    def __init__(self):
        self.aa=[]


    def push(self, x: int) -> None:
         self.aa.append(x)


    def pop(self) -> None:
         self.aa.pop()

    def top(self) -> int:
       return self.aa[-1]

    def min(self) -> int:
        return min(self.aa)