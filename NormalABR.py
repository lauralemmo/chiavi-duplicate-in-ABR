from Node import Node


class NormalABR:

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
        if (key <= currentNode.key):
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
        elif (key < currentNode.key):
            pNode = currentNode
            self.search(pNode, currentNode.left, key)
        else:
            pNode = currentNode
            self.search(pNode, currentNode.right, key)


    def deleteNode(self, pNode, removableNode):
        if (removableNode.left == None):
            self.modify(pNode, removableNode, removableNode.right)
        elif (removableNode.right == None):
            self.modify(pNode, removableNode, removableNode.left)
        else:
            minimumNode = self.minimum(removableNode.right)   #parametri
            if (minimumNode):                                 #condizione if
                self.modify(..., minimumNode, minimumNode.right)   #mi serve il padre
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


    def minimum(self, newNode):            #devo fornire anche il padre
        if (newNode.left != None):
            self.minimum(newNode.left)
        return newNode


