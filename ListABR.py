#from Node import Node


#class Node:

#    def __init__(self, key, init_data):
#        self.key = key
#        self.left = None
#        self.right = None
#        self.next = None



class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.next = None
        self.head = None




class ListABR:

    def __init__(self):
        self.root = None


    def setRoot(self, key):
        self.root = LinkedListNode(key)
        LinkedListNode(key).head = self.root

    def insert(self, key):
        if (self.root is None):
           self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if (key == currentNode.key):
            currentNode.next = Node(key)
            currentNode.
        elif (key < currentNode.key):
            if (currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if (currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)



    #SISTEMA NODI CHE HANNO SET E GET SOLO NELLA CLASSE NODE
    #MENTRE QUELLE MESSE NELLE ALTRE CLASSI NON HANNO METODI
    #PROVA A TOGLIERE IMPORT E GUARDA SE FUNZIONA LO STESSO