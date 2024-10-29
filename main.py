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
normalABR.delete(2)
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





nRipetizioni = 2000
nElementi = 1000
nMaxDisponibile = 650


mediaTempi1 = []
def tempoInserimentoNormalABR():
    sommaTempiInserimento = []
    for k in range(0, nRipetizioni):
        albero1 = NormalABR()     # ogni volta si riparte da un albero vuoto e si inseriscono esattamente 'nElementi' elementi
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero1.insert(key)
            end = timer()
            tEsecuzione = end - start

            if(k == 0):
                sommaTempiInserimento.append(tEsecuzione)
            else:
                sommaTempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiInserimento[i] / nRipetizioni
        mediaTempi1.append(media)


def graficoInserimentoNormalABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi1
    plt.plot(x, y, color="red")
    plt.title('inserimento normal ABR')
    plt.show()




mediaTempi2 = []
def tempoInserimentoBooleanABR():
    sommaTempiInserimento = []
    for k in range(0, nRipetizioni):
        albero2 = BooleanABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero2.insert(key)
            end = timer()
            tEsecuzione = end - start

            if (k == 0):
                sommaTempiInserimento.append(tEsecuzione)
            else:
                sommaTempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiInserimento[i] / nRipetizioni
        mediaTempi2.append(media)


def graficoInserimentoBooleanABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi2
    plt.plot(x, y, color="blue")
    plt.title('inserimento boolean ABR')
    plt.show()




mediaTempi3 = []
def tempoInserimentoListABR():
    sommaTempiInserimento = []
    for k in range(0, nRipetizioni):
        albero3 = ListABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            start = timer()
            albero3.insert(key)
            end = timer()
            tEsecuzione = end - start

            if (k == 0):
                sommaTempiInserimento.append(tEsecuzione)
            else:
                sommaTempiInserimento[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiInserimento[i] / nRipetizioni
        mediaTempi3.append(media)


def graficoInserimentoListABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi3
    plt.plot(x, y, color="green")
    plt.title('inserimento list ABR')
    plt.show()




mediaTempi4 = []
def tempoCancellazioneNormalABR():
    sommaTempiCancellazione = []
    for k in range(0, nRipetizioni):
        albero4 = NormalABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            albero4.insert(key)
            start = timer()
            albero4.delete(key)
            end = timer()
            albero4.insert(key)
            tEsecuzione = end - start

            if (k == 0):
                sommaTempiCancellazione.append(tEsecuzione)
            else:
                sommaTempiCancellazione[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiCancellazione[i] / nRipetizioni
        mediaTempi4.append(media)


def graficoCancellazioneNormalABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi4
    plt.plot(x, y, color="red")
    plt.title('cancellazione normal ABR')
    plt.show()




mediaTempi5 = []
def tempoCancellazioneBooleanABR():
    sommaTempiCancellazione = []
    for k in range(0, nRipetizioni):
        albero5 = BooleanABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            albero5.insert(key)
            start = timer()
            albero5.delete(key)
            end = timer()
            albero5.insert(key)
            tEsecuzione = end - start

            if (k == 0):
                sommaTempiCancellazione.append(tEsecuzione)
            else:
                sommaTempiCancellazione[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiCancellazione[i] / nRipetizioni
        mediaTempi5.append(media)


def graficoCancellazioneBooleanABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi5
    plt.plot(x, y, color="blue")
    plt.title('cancellazione boolean ABR')
    plt.show()




mediaTempi6 = []
def tempoCancellazioneListABR():
    sommaTempiCancellazione = []
    for k in range(0, nRipetizioni):
        albero6 = ListABR()
        for i in range(0, nElementi):
            key = random.randint(0, nMaxDisponibile)
            albero6.insert(key)
            start = timer()
            albero6.delete(key)
            end = timer()
            albero6.insert(key)
            tEsecuzione = end - start

            if (k == 0):
                sommaTempiCancellazione.append(tEsecuzione)
            else:
                sommaTempiCancellazione[i] += tEsecuzione

    for i in range(0, nElementi):
        media = sommaTempiCancellazione[i] / nRipetizioni
        mediaTempi6.append(media)


def graficoCancellazioneListABR():
    x = np.arange(0, nElementi, 1)
    y = mediaTempi6
    plt.plot(x, y, color="green")
    plt.title('cancellazione list ABR')
    plt.show()




def graficiInserimento():
    x = np.arange(0, nElementi, 1)
    y1 = mediaTempi1
    y2 = mediaTempi2
    y3 = mediaTempi3
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.title('inserimenti in ABR')
    plt.legend(['normal abr', 'boolean abr', 'list abr'])
    plt.show()


def graficiCancellazione():
    x = np.arange(0, nElementi, 1)
    y1 = mediaTempi4
    y2 = mediaTempi5
    y3 = mediaTempi6
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.title('cancellazioni in ABR')
    plt.legend(['normal abr', 'boolean abr', 'list abr'])
    plt.show()





if __name__ == '__main__':
    tempoInserimentoNormalABR()
    graficoInserimentoNormalABR()
    tempoInserimentoBooleanABR()
    graficoInserimentoBooleanABR()
    tempoInserimentoListABR()
    graficoInserimentoListABR()
    tempoCancellazioneNormalABR()
    graficoCancellazioneNormalABR()
    tempoCancellazioneBooleanABR()
    graficoCancellazioneBooleanABR()
    tempoCancellazioneListABR()
    graficoCancellazioneListABR()
    graficiInserimento()
    graficiCancellazione()
