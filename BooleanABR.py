from Node import Node



class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.flag = True






class BooleanABR:

    def __init__(self):
        self.root = None


    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if (self.root is None):
           self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if (key == currentNode.key):
            if (currentNode.flag):
                currentNode.left = Node(key)
                currentNode.flag = False
            else:
                currentNode.right = Node(key)
                currentNode.flag = True

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
