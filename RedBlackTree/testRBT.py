#! /usr/bin/env python3
import rbt

def main():
    tree = rbt.RedBlackTree()
    tree.insert(14)
    tree.insert(42)
    tree.insert(35)
    tree.insert(7)
    tree.insert(26)
    tree.insert(17)
    rbt.preorder(tree.root)
    

main()