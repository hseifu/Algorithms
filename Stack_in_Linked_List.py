#! /usr/bin/env python3

class Stack:
    class StackNode:
        def __init__(self, initData):
            self.data = initData
            self.next = None

    #Constructor runs in constant time
    def __init__(self):
        self.__head = None
        self.__size = -1

    #Push function runs in constant time
    def push(self,x): 
        if self.head == None:
            self.head = x
            x.next = None
        else:
            x.next = self.head
            head = x
            size += 1
    
    #Pop function runs in constant time
    def pop(self):
        if size == -1:
            raise IndexError("Popping stack underflow")
        elif size == 0:
            temp = self.head
            self.head = None 
            self.size -= 1
            return temp
        else:
            temp = self.head
            del self.head
            self.head = temp.next
            self.size -= 1
            return temp
    
    #Check if empty function runs in constant time
    def isEmpty(self):
        if size == -1:
            return True
        else:
            return False
            


        