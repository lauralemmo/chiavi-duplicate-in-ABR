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
        l = LinkedListNode(key)
        self.root = l
        l.head = Node()

    def insert(self, key):
        if (self.root is None):
           self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentList, key):
        if (key == currentList.key):
            n = Node()
            n.next = currentList.head           #aggiungo in testa
            currentList.head = n
        elif (key < currentList.key):
            if (currentList.left):
                self.insertNode(currentList.left, key)
            else:
                l = LinkedListNode(key)
                currentList.left = l
                l.head = Node()
        elif (key > currentList.key):
            if (currentList.right):
                self.insertNode(currentList.right, key)
            else:
                l = LinkedListNode(key)
                currentList.right = l
                l.head = Node()



    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentList, key):
        if (currentList is None):
            return False
        elif (key == currentList.key):
            return True
        elif (key < currentList.key):
            return self.findNode(currentList.left, key)
        else:
            return self.findNode(currentList.right, key)





    def delete(self, key):
        self.search(None, self.root, key)


    def search(self, pList, currentList, key):
        if (currentList is None):
            return False
        elif (currentList.key == key):
            self.deleteNode(pList, currentList)
        elif (key < currentList.key):
            pList = currentList
            self.search(pList, currentList.left, key)
        else:
            pList = currentList
            self.search(pList, currentList.right, key)


    def deleteNode(self, pList, listRemovableNode):
        if (listRemovableNode.head.next == None):
            if (listRemovableNode.left == None):
                self.modify(pList, listRemovableNode, listRemovableNode.right)
            elif (listRemovableNode.right == None):
                self.modify(pList, listRemovableNode, listRemovableNode.left)
            else:
                minimumList, pMinimumList = self.minimum(listRemovableNode, listRemovableNode.right)
                if (pMinimumList != listRemovableNode):
                    self.modify(pMinimumList, minimumList, minimumList.right)
                    minimumList.right = listRemovableNode.right
                self.modify(pList, listRemovableNode, minimumList)
                minimumList.left = listRemovableNode.left
        else:
            listRemovableNode.head = listRemovableNode.head.next


    def modify(self, pList, listRemovableNode, newList):
        if (pList is None):
            self.root = newList
        elif (listRemovableNode == pList.left):
            pList.left = newList
        else:
            pList.right = newList


    def minimum(self, pNode, newNode):
        if (newNode.left != None):
            pNode = newNode
            self.minimum(pNode, newNode.left)
        return newNode, pNode
