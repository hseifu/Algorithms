#! /usr/bin/env python3
class StackNode:
        def __init__(self, initData):
            self.data = initData
            self.next = None
class Stack:
    

    #Constructor runs in constant time
    def __init__(self):
        self.__head = None
        self.__size = -1

    #Check if empty function runs in constant time
    def isEmpty(self):
        if self.__size == -1:
            return True
        else:
            return False

    #Push function runs in constant time
    def push(self,data):
        x = StackNode(data)
        if self.__head == None:
            self.__head = x
            x.next = None
        else:
            x.next = self.__head
            self.__head = x
        self.__size += 1
    
    #Pop function runs in constant time
    def pop(self):
        if self.isEmpty():
            raise IndexError("Popping stack underflow")
        elif self.__size == 0:
            temp = self.__head
            self.__head = None 
            self.__size -= 1
            return temp.data
        else:
            temp = self.__head
            del self.__head
            self.__head = temp.next
            self.__size -= 1
            return temp.data
    
    
            
def main():
    S = Stack()
    S.push(1)
    S.push(2)
    print(S.pop())
    print(S.pop())
    print(S.isEmpty())
    try:
        print(S.pop())
    except ValueError as err:
        print(err.args)
    
main()
        