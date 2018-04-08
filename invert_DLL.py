#! /usr/bin/env python3
class DoublyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def add(self,val):
        new = DoublyLinkedNode(val)
        new.next = None
        new.prev = self.last
        if self.first == self.last == None:
            self.first = self.last = new
        else:
            self.last.next = new
        self.last = new
        self.size += 1
    def show(self):
        cursor = self.first
        for i in range(self.size):
            print(cursor.val)
            cursor = cursor.next

#inverting function that runs in linear time and is in-situ
def invert(A):
    cursor = A.first
    for i in range(A.size):
        temp = cursor.next
        cursor.next = cursor.prev
        cursor.prev = temp
        cursor = cursor.prev
    temp = A.first
    A.first = A.last
    A.last = temp

def main():
    DDL = DoublyLinkedList()
    DDL.add(3)
    DDL.add(5)
    DDL.show()
    invert(DDL)
    DDL.show()

main()