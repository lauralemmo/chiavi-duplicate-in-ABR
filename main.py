from BooleanABR import BooleanABR
from NormalABR import NormalABR

normalABR = NormalABR()
normalABR.insert(7)
normalABR.insert(1)
normalABR.insert(4)
normalABR.insert(10)
normalABR.insert(8)
print("albero ordinato: ")
normalABR.inorder()
normalABR.delete(4)
print("\nalbero dopo cancellazione: ")
normalABR.inorder()

booleanABR = BooleanABR()