import random
import matplotlib.pyplot as plt
import numpy as np

from BooleanABR import BooleanABR
from ListABR import ListABR
from NormalABR import NormalABR
from timeit import default_timer as timer

normalABR = NormalABR()
normalABR.insert(7)
normalABR.insert(1)
normalABR.insert(4)
normalABR.insert(10)
normalABR.insert(8)
normalABR.insert(7)
print("albero ordinato: ")
normalABR.inorder()
normalABR.delete(4)
print("\nalbero dopo cancellazione: ")
normalABR.inorder()
print("\nnodo presente: ", normalABR.find(1))
print("\nnodo presente: ", normalABR.find(5))

booleanABR = BooleanABR()
booleanABR.insert(2)
booleanABR.insert(8)
booleanABR.insert(5)
booleanABR.insert(8)
print("\nalbero ordinato: ")
booleanABR.inorder()
booleanABR.delete(8)
print("\nalbero dopo cancellazione: ")
booleanABR.inorder()
booleanABR.insert(3)
print("\nalbero ordinato: ")
booleanABR.inorder()
print("\nnodo presente: ", booleanABR.find(8))
print("\nnodo presente: ", booleanABR.find(5))

listABR = ListABR()
listABR.insert(11)
listABR.insert(12)
listABR.insert(4)
listABR.insert(10)
listABR.insert(8)
listABR.insert(11)
listABR.insert(11)
print("\nalbero ordinato: ")
listABR.inorder()
listABR.delete(11)
listABR.delete(11)
print("\nalbero dopo cancellazione: ")
listABR.inorder()
print("\nnodo presente: ", listABR.find(12))
print("\nnodo presente: ", listABR.find(1))







print("\n\n\n\n")


def tempoInserimentoNormalABR():
    sommatempiInserimento = []
    mediaTempi = []
    for k in range(0, 10000):
        albero = NormalABR()                  #VOGLIO CHE OGNI VOLTA SI RIPARTA DA UN NUOVO ALBERO VUOTO
        for i in range(0, 100):              #NE INSERISCO 100 O UNO OGNI 10?
            key = random.randint(0, 80)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            # if(k == 1):
            #    sommatempiInserimento[i] = sommatempiInserimento[i-1] + tEsecuzione
            # else:
            #    sommatempiInserimento[i] += sommatempiInserimento[i - 1] + tEsecuzione

            if(k == 0):
                sommatempiInserimento.append(tEsecuzione)
                #sommatempiInserimento[i] = tEsecuzione
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(0, 100):
        media = sommatempiInserimento[i] / 10000
        mediaTempi.append(media)





    x = np.arange(0, 100, 1)
    y = mediaTempi
    plt.plot(x, y)
    plt.show()







def tempoInserimentoBooleanABR():
    sommatempiInserimento = []
    mediaTempi = []
    for k in range(1, 10000):
        albero = BooleanABR()
        for i in range(1, 100):
            key = random.randint(0, 80)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            #if(k == 1):
            #    sommatempiInserimento[i] = sommatempiInserimento[i-1] + tEsecuzione
            #else:
            #    sommatempiInserimento[i] += sommatempiInserimento[i - 1] + tEsecuzione

            if(k == 1):
                # sommatempiInserimento.append(tEsecuzione)
                sommatempiInserimento[i] = tEsecuzione
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(1, 100):
        mediaTempi[i] = sommatempiInserimento[i] / 10000







def tempoInserimentoListABR():
    sommatempiInserimento = []
    mediaTempi = []
    for k in range(1, 10000):
        albero = ListABR()
        for i in range(1, 100):
            key = random.randint(0, 80)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            #if(k == 1):
            #    sommatempiInserimento[i] = sommatempiInserimento[i-1] + tEsecuzione
            #else:
            #    sommatempiInserimento[i] += sommatempiInserimento[i - 1] + tEsecuzione

            if(k == 1):
                # sommatempiInserimento.append(tEsecuzione)
                sommatempiInserimento[i] = tEsecuzione
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(1, 100):
        mediaTempi[i] = sommatempiInserimento[i] / 10000









if __name__ == '__main__':
    tempoInserimentoNormalABR()