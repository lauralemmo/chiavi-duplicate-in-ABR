import random
import matplotlib.pyplot as plt
import numpy as np

from BooleanABR import BooleanABR
from ListABR import ListABR
from NormalABR import NormalABR
from timeit import default_timer as timer

#import sys
#sys.setrecursionlimit(10**6)

normalABR = NormalABR()
normalABR.insert(7)
normalABR.insert(1)
normalABR.insert(4)
normalABR.insert(10)
normalABR.insert(8)
normalABR.insert(7)
print("albero ordinato: ")
normalABR.inorder()
normalABR.search(4)
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
booleanABR.delete(8)                     #DEVO METTERE ANCHE SEARCH    E SE PROVO A CANCELLARE UN NODO NON PRESENTE?
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
listABR.delete(11)                #ANCHE SEARCH
listABR.delete(11)
print("\nalbero dopo cancellazione: ")
listABR.inorder()
print("\nnodo presente: ", listABR.find(12))
print("\nnodo presente: ", listABR.find(1))







print("\n\n\n\n")







nRipetizioni = 2000
nElementi = 900
nMaxDisponibile = 650


mediaTempi1 = []
def tempoInserimentoNormalABR():
    sommatempiInserimento = []
    for k in range(0, nRipetizioni):
        albero = NormalABR()                  #VOGLIO CHE OGNI VOLTA SI RIPARTA DA UN NUOVO ALBERO VUOTO
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            if(k == 0):
                sommatempiInserimento.append(tEsecuzione)
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommatempiInserimento[i] / nRipetizioni
        mediaTempi1.append(media)


def graficoInserimentoNormalABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi1
    plt.plot(x, y)
    plt.title('inserimento normal ABR')
    plt.show()




mediaTempi2 = []
def tempoInserimentoBooleanABR():
    sommatempiInserimento = []
    for k in range(0, nRipetizioni):
        albero = NormalABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            if (k == 0):
                sommatempiInserimento.append(tEsecuzione)
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommatempiInserimento[i] / nRipetizioni
        mediaTempi2.append(media)


def graficoInserimentoBooleanABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi2
    plt.plot(x, y)
    plt.title('inserimento boolean ABR')
    plt.show()




mediaTempi3 = []
def tempoInserimentoListABR():
    sommatempiInserimento = []
    for k in range(0, nRipetizioni):
        albero = NormalABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero.insert(key)
            end = timer()
            tEsecuzione = end - start

            if (k == 0):
                sommatempiInserimento.append(tEsecuzione)
            else:
                sommatempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommatempiInserimento[i] / nRipetizioni
        mediaTempi3.append(media)


def graficoInserimentoListABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi3
    plt.plot(x, y)
    plt.title('inserimento list ABR')
    plt.show()












mediaTempi4 = []
def tempoCancellazioneNormalABR():
    sommatempiCancellazione = []
    for k in range(0, nRipetizioni):
        albero = NormalABR()                    #VOGLIO CHE OGNI VOLTA SI RIPARTA DA UN ALBERO NUOVO
        albero.creazioneAlbero(nElementi, nMaxDisponibile)
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero.search(key)
            albero.delete(key)
            end = timer()
            tEsecuzione = end - start

            if(k == 0):
                sommatempiCancellazione.append(tEsecuzione)
            else:
                sommatempiCancellazione[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommatempiCancellazione[i] / nRipetizioni
        mediaTempi4.append(media)


def graficoCancellazioneNormalABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi4
    plt.plot(x, y)
    plt.title('cancellazione normal ABR')
    plt.show()





#CORREGGI I DELETE E I SEARCH SIA QUI SIA NELLE CLASSI BOOLEAN E LIST CHE ANCORA NON HO CAMBIATO
#LE DEVO METTERE COME NORMAL










if __name__ == '__main__':
    tempoInserimentoNormalABR()
    graficoInserimentoNormalABR()
    tempoInserimentoBooleanABR()
    graficoInserimentoBooleanABR()
    tempoInserimentoListABR()
    graficoInserimentoListABR()
    tempoCancellazioneNormalABR()
    graficoCancellazioneNormalABR()