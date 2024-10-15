from NormalABR import NormalABR

normalABR = NormalABR()

normalABR.insert(7)
normalABR.insert(1)
normalABR.insert(4)
normalABR.insert(10)
normalABR.insert(8)

normalABR.inorder()
print("\n")

normalABR.delete(4)

normalABR.inorder()