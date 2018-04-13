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

    def _rotateLeft_(self, node):                 #Keeps RBT property even when implemented like a BST
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
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
                if y.color is Color.RED:          #Case 1 uncle is red
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
        y = node
        y_original_color = y.color                      #save the color. needed at the end
        if node.left is None:                           #check if node children are nil
            x = node.right                              #save the node to be transplanted into
            self.transplant(node, node.right)
        elif node.right is None:
            x = node.left                               #save the node to be transplanted into
            self.transplant(node, node.left)
        else:                                           #if it doesnt have a nil child
            y = node.right.minimum()
            y_original_color = y.color                  #new original color because we are in this case                                   
            x = y.right                                 #concerened with the node that is going to be taken up
            if y.parent == node:                        #make child of node to be deleted, child of succesor node
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color                        #do all steps as a BST then finally change color
        if y_original_color is Color.BLACK:             #if initial color was red everything is good,
            self.RB_delete_fixup(node)                  #otherwise we have to fix our tree

    def RB_delete_fixup(self, node):                    #fix up function for delete
        while node is not self.__root and node.color is Color.BLACK:  #only works when node is not root and color is black
            if node is node.parent.left:                #Symmetric Case 1 when node is left child
                w = node.parent.right                   #get sibling
                if w.color is Color.RED:                #Case 1: sibling is red
                    w.color = Color.BLACK               #if sibling is red, change sibling to black
                    node.parent.color = Color.RED       #then change node to black
                    self._rotateLeft_(node.parent)      #rotate parent then everything is fixed for upper part then we are in second case
                if w.left.color is w.right.color is Color.BLACK:    #Case 2 sibling and sibling's children are both black
                    w.color = Color.RED                 #change sibling's color. Note that "if" is used and not elif since we want to accept from case 1 also
                    node = node.parent                  #move node to parent since now we want to study the implications of changing sibling to red
                else:
                    if w.right.color is Color.BLACK:    #Case 3 left child of sibling is red
                        w.left.color = Color.BLACK          #change left child of sibling to black
                        w.color = Color.RED             #change sibling color to red
                        self._rotateRight_(w)           #make sibling go down and become right child of left child
                        w = node.parent.right           #make sibling point to the black parent node with right child red
                    w.color = node.parent.color         #Case 4: (accepts changed version of case 3) sibling has right red child
                    node.parent.color = Color.BLACK     #Change sibling color to node parent color then change node parent color to black
                    w.right.color = Color.BLACK         #Change right child of sibling's color to black
                    self._rotateLeft_(node.parent)      #rotate left node's parent and make it sibling's child
                    x = self.__root                     #change which node to check for tree property
            else:                                       #Symmetric Case 2 when node is right a node
                w = node.parent.left                   
                if w.color is Color.RED:                
                    w.color = Color.BLACK               
                    node.parent.color = Color.RED       
                    self._rotateRight_(node.parent)      
                if w.left.color is w.right.color is Color.BLACK:    
                    w.color = Color.RED                 
                    node = node.parent                  
                else:
                    if w.left.color is Color.BLACK:    
                        w.right.color = Color.BLACK          
                        w.color = Color.RED             
                        self._rotateLeft_(w)           
                        w = node.parent.left           
                    w.color = node.parent.color         
                    node.parent.color = Color.BLACK     
                    w.left.color = Color.BLACK       
                    self._rotateRight_(node.parent)      
                    x = self.__root
        x.color = Color.BLACK

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
    if root_node == None:
        return
    print(root_node.data, root_node.color)
    preorder(root_node.left)
    preorder(root_node.right)

