import random

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
                currentNode.flag = False
                if (currentNode.left):
                    self.insertNode(currentNode.left, key)
                else:
                    currentNode.left = Node(key)
            else:
                currentNode.flag = True
                if (currentNode.right):
                    self.insertNode(currentNode.right, key)
                else:
                    currentNode.right = Node(key)
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


    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)




    def delete(self, key):
        self.search(None, self.root, key)


    def search(self, pNode, currentNode, key):
        if (currentNode is None):
            return False
        elif (currentNode.key == key):
            self.deleteNode(pNode, currentNode)
            return True
        elif (key < currentNode.key):
            pNode = currentNode
            return self.search(pNode, currentNode.left, key)
        else:
            pNode = currentNode
            return self.search(pNode, currentNode.right, key)


    def deleteNode(self, pNode, removableNode):
        if (removableNode.left == None):
            self.modify(pNode, removableNode, removableNode.right)
        elif (removableNode.right == None):
            self.modify(pNode, removableNode, removableNode.left)
        else:
            minimumNode, pMinimumNode = self.minimum(removableNode, removableNode.right)
            if (pMinimumNode != removableNode):
                self.modify(pMinimumNode, minimumNode, minimumNode.right)
                minimumNode.right = removableNode.right
            self.modify(pNode, removableNode, minimumNode)
            minimumNode.left = removableNode.left


    def modify(self, pNode, removableNode, newNode):
        if (pNode is None):
            self.root = newNode
        elif (removableNode == pNode.left):
            pNode.left = newNode
        else:
            pNode.right = newNode


    def minimum(self, pNode, newNode):
        if (newNode.left != None):
            pNode = newNode
            return self.minimum(pNode, newNode.left)
        else:
            return newNode, pNode




    def inorder(self):
        self.inorderTree(self.root)


    def inorderTree(self, node):
        if (node != None):
            self.inorderTree(node.left)
            print(node.key)
            self.inorderTree(node.right)


    def creazioneAlbero(self, nElementi, nMaxDisponibile):
        for i in range (0, nElementi):
            n = random.randint(0, nMaxDisponibile)
            self.insert(n)