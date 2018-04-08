#! /usr/bin/env python3

#Binary Search Tree Node
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

#Binary Search Tree with method to insert value
class BSTList:
    def __init__(self):
        self.head = None
    def add(self, val):
        new = BSTNode(val)
        y = None
        x = self.head
        
        while x != None:
            y = x
            if new.val < x.val:
                x = x.left
            else:
                x = x.right
        new.parent = y
        if y == None:
            self.head = new
        elif new.val < y.val:
            y.left = new
        else:
            y.right = new

#function for printing a BST in correct order
#takes the BST's head as parameter
def show(BST_Node):
    if BST_Node == None:
        return
    show(BST_Node.left)
    print(BST_Node.val)
    show(BST_Node.right) 


#Linked list node
class LinkNode:
    def __init__(self, initData):
        self.data = initData
        self.next = None
#linked list with methods to add to a linked
#list and method to show values in order 
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    #operation runs in linear time
    def add(self, data):
        new = LinkNode(data)
        if self.head == None:
            self.head = new
        else:
            cursor = self.head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = new
        self.size += 1
    def show(self):
        cursor = self.head
        for i in range(self.size):
            print(cursor.data)
            cursor = cursor.next

#Better implementation of linked list that takes
#constant time to add a value because last element 
#is known
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #operation runs in constant time
    def add(self, data):
        new = LinkNode(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
            self.size += 1
    def show(self):
        cursor = self.head
        for i in range(self.size):
            print(cursor.data)
            cursor = cursor.next

#function for iterating through a BST
#in order and adding to a list, each value
#runs in O(number of nodes * run time for add)
def BST_to_LL(BST_Node, lstofvals):
    if BST_Node == None:
        return
    BST_to_LL(BST_Node.left, lstofvals)
    lstofvals.add(BST_Node.val)
    BST_to_LL(BST_Node.right, lstofvals)     

#function for converting a linked list into a BST
#Runs in O(nlogn)
def LL_to_BST(BST, lstofvals):
    cursor = lstofvals.head
    #iterating through entire list runs in linear 
    for i in range(lstofvals.size):
        #adding a value to a BST runs in logarithmic
        #time
        BST.add(cursor.data)
        cursor = cursor.next

#test function
def main():
    T = BSTList()
    T_copy = BSTList()
    L = LinkedList()
    L2 = LinkedList2()
    T.add(12)
    T.add(5)
    T.add(2)
    T.add(9)
    T.add(18)
    T.add(15)
    T.add(19)
    T.add(13)
    T.add(17)
    BST_to_LL(T.head, L)
    BST_to_LL(T.head, L2)
    print("The sorted form of the BST as a list is:")
    L.show()
    print("Now using modified list")
    L2.show()
    print("Making a BST from the list above")
    LL_to_BST(T_copy, L)
    show(T_copy.head)

main()

    



    