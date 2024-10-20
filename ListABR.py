#from Node import Node


#class Node:

#    def __init__(self, key, init_data):
#        self.key = key
#        self.left = None
#        self.right = None
#        self.next = None




class Node:
    def __init__(self):
        self.next = None


class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.head = None




class ListABR:

    def __init__(self):
        self.root = None


    def setRoot(self, key):
        a = LinkedListNode(key)
        self.root = a
        a.head = Node()                               #METTI N AL POSTO DI A PER NODI E L PER LISTE

    def insert(self, key):
        if (self.root is None):
           self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentList, key):
        if (key == currentList.key):
            a = Node()
            a.next = currentList.head     #aggiungo in testa
            currentList.head = a
        elif (key < currentList.key):
            if (currentList.left):
                self.insertNode(currentList.left, key)
            else:
                a = LinkedListNode(key)
                currentList.left = a
                a.head = Node()
        elif (key > currentList.key):
            if (currentList.right):
                self.insertNode(currentList.right, key)
            else:
                a = LinkedListNode(key)
                currentList.right = a
                a.head = Node()
