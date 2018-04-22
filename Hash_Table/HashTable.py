#! /usr/bin/env python3
import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.__maxSize = 100 #max size
        self.__currentSize = 0
        self.__arr = [] #array to contain pointers to nodes
        for _ in range(self.__maxSize):
            self.__arr.append(None)
    
    def hashCode(self, key):
        return key % self.__maxSize
    
    def insertNode(self, key, value):
        a = Node(key, value)
        for i in range(self.__maxSize):
            new_key = (self.hashCode(key) + i) % self.__maxSize
            if self.__arr[new_key] == None:
                self.__arr[new_key] = a #
                self.__currentSize += 1
                break

    def find(self, key):
        new_key = self.hashCode(key)
        i = 0
        while self.__arr[new_key + i] != None:
            if self.__arr[new_key + i].key == key:
                return self.__arr[new_key + i].value
            i += 1
            if i == self.__maxSize:
                break
        return None

    def isEmpty(self):
        return self.__currentSize == 0

def main():
    HT = HashTable()
    k = HT.insertNode(170, 9)
    j = HT.insertNode(70, 32)
    print(HT.find(170))
    print(HT.find(70))
    

main()





