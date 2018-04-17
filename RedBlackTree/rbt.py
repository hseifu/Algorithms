#! /usr/bin/env python3
from enum import Enum

Color = Enum("Color", "RED BLACK")

class Node:
    def __init__(self, data, color = Color.RED):
        self.data = data 
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def _rotateLeft_(self, node):                 #Keeps RBT property even when implemented like a BST
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.__root = y
        elif node is node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y
        
    def _rotateRight_(self, node):                #Keeps RBT property even when implemented like a BST
        y = node.left
        node.left = y.right
        if y.right is not None:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.__root = y
        elif node is node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert(self, val):
        z = Node(val)                             #create node to be added
        y = None
        x = self.__root
        while x != None:                          #iterate down until the iterators child is null
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y                              #parent of node to be added is the node pointed by the cursor
        if y == None:                             #if the cursor is still pointing to nil that means there was 
            self.__root = z                       #no root node so assign new node as root node                              
        elif z.data < y.data:                     #if the new data is less than the parent data then make it left
            y.left = z
        else:                                     #if not then make it right
            y.right = z
        self.RB_insert_fixup(z)               #then fixup your red and black tree if grandparent exists

    def RB_insert_fixup(self, z):
        while z.parent is not None and z.parent.parent is not None and z.parent.color == Color.RED:
            if z.parent is z.parent.parent.left:  #check if parent is left or right child
                y = z.parent.parent.right         #uncle is on the right of grand parent
                if y is not None and y.color is Color.RED:          #Case 1 uncle is red
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:                              #Case 2 and 3 black uncle
                    if z is z.parent.right:        #Case 2 right child
                        z = z.parent
                        self._rotateLeft_(z)       #rotate and go to Case 3
                    z.parent.color = Color.BLACK   #Case 3
                    z.parent.parent.color = Color.RED
                    self._rotateRight_(z.parent.parent)
            else:                                 
                y = z.parent.parent.left            #uncle is on the left of grand parent
                if y is not None and y.color is Color.RED:            #Case 1 uncle is red
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:                                #Case 2 and 3 black uncle
                    if z is z.parent.left:           #Case 2 left child
                        z = z.parent
                        self._rotateRight_(z)        #rotate and go to Case 3
                    z.parent.color = Color.BLACK     #Case 3
                    z.parent.parent.color = Color.RED
                    self._rotateLeft_(z.parent.parent)
        self.__root.color = Color.BLACK              #changing the root color to black

    def transplant(self, u, v):                      #replace u with v implemented like a BST
        if u.parent is None:
            self.__root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, node):
        x = None
        y = None                      #save the color. needed at the end
        yisLeft = False
        if node.left is None or node.right is None:
            y = node
        else:
            y = self.successor(node)
        if y.left is not None:
            x = y.left
        else:           
            x = y.right
        if x is None:
            x = Node(None)
            x.color = Color.BLACK
        if x is not None:
            x.parent = y.parent
        xparent = y.parent
        if y.parent is None:
            self.__root = x                  #otherwise we have to fix our tree
        elif y is y.parent.left:
            y.parent.left = x
            yisLeft = True
        else:
            y.parent.right = x
            yisLeft = False
        if y is not node:
            node.data = y.data
        if y.color is Color.BLACK:
            self.RB_delete_fixup(x, xparent, yisLeft)


    def RB_delete_fixup(self, node, nodeParent, nodeisLeft):                    #fix up function for delete
        while node is not self.__root and node.color is Color.BLACK:  #only works when node is not root and color is black
            if nodeisLeft:                #Symmetric Case 1 when node is left child
                w = nodeParent.right                   #get sibling
                if w.color is Color.RED:                #Case 1: sibling is red
                    w.color = Color.BLACK               #if sibling is red, change sibling to black
                    node.parent.color = Color.RED       #then change node to black
                    self._rotateLeft_(nodeParent)      #rotate parent then everything is fixed for upper part then we are in second case
                    w = node.parent.right
                if w.left is not None and w.right is not None and (w.left.color is w.right.color is Color.BLACK):    #Case 2 sibling and sibling's children are both black
                    w.color = Color.RED                 #change sibling's color. Note that "if" is used and not elif since we want to accept from case 1 also
                    node = nodeParent    
                    nodeParent = node.parent
                    if node is nodeParent.left:
                        nodeisLeft = True
                    else:
                        nodeisLeft = False              #move node to parent since now we want to study the implications of changing sibling to red
                else:
                    if w.right is not None and w.right.color is Color.BLACK:    #Case 3 left child of sibling is red
                        w.left.color = Color.BLACK          #change left child of sibling to black
                        w.color = Color.RED             #change sibling color to red
                        self._rotateRight_(w)           #make sibling go down and become right child of left child
                        w = nodeParent.right           #make sibling point to the black parent node with right child red
                    w.color = nodeParent.color         #Case 4: (accepts changed version of case 3) sibling has right red child
                    nodeParent.color = Color.BLACK     #Change sibling color to node parent color then change node parent color to black
                    if w.right is not None:
                        w.right = Color.BLACK         #Change right child of sibling's color to black
                    self._rotateLeft_(nodeParent)      #rotate left node's parent and make it sibling's child
                    node = self.__root
                    nodeParent = None                     #change which node to check for tree property
            else:                                       #Symmetric Case 2 when node is right a node
                w = node.parent.left                   
                if w.color is Color.RED:                
                    w.color = Color.BLACK               
                    nodeParent.color = Color.RED       
                    self._rotateRight_(nodeParent)      
                    w = nodeParent.left  
                if w.left is not None and w.right is not None and (w.left.color is w.right.color is Color.BLACK):    
                    w.color = Color.RED                 
                    node = nodeParent
                    nodeParent = node.parent
                    if node is nodeParent.left:
                        nodeisLeft = True
                    else:
                        node = False                  
                else:
                    if w.left is not None and w.left.color is Color.BLACK:    
                        w.right.color = Color.BLACK          
                        w.color = Color.RED             
                        self._rotateLeft_(w)           
                        w = nodeParent.left           
                    w.color = nodeParent.color         
                    nodeParent.color = Color.BLACK     
                    if w.left is not None:
                        w.left = Color.BLACK
                    self._rotateRight_(nodeParent)      
                    node = self.__root
                    nodeParent = None
        node.color = Color.BLACK

    def predecessor(self, node):
        #return prev
        if node.left is not None:
            return self.getMaximum(node.left)
        y = node.parent
        while y is not None and node is y.left:
            node = y
            y = y.parent
        return y

    def successor(self, node):
        #return next
        if node.right is not None:
            return self.getMinimum(node.right)
        y = node.parent
        while y is not None and node is y.right:
            node = y
            y = y.parent
        return y

    def getMinimum(self, node):
        #return minimum node
        while node.left is not None:
            node = node.left 
        return node
        
    def getMaximum(self, node):
        #return max node
        while node.right is not None:
            node = node.right
        return node

    def search(self,val):
        x = self.__root
        #search for val
        while x is not None and val is not x.data:
            if val < x.data:
                x = x.left
            else:
                x = x.right
        return x

def preorder(root_node):
    if root_node == None or root_node.data == None:
        return
    print(root_node.data, end = "") 
    if root_node.color == Color.BLACK:
        print("B ", end = "")
    else:
        print("R ", end = "")
    preorder(root_node.left)
    preorder(root_node.right)

