"""
Scrivi un programma che chieda all’utente di inserire una lista di numeri interi.
Usa funzioni e cicli per:
● calcolare la media dei numeri
● contare quanti numeri sono sopra la media e quanti sotto
● creare una nuova lista contenente solo i numeri maggiori della media
● determinare la lunghezza della sequenza più lunga di numeri consecutivi uguali
"""

# Funzione per la lettura dei numeri
def leggiNum():
    numeri =[]
    n= int(input('Quanti numeri vuoi inserire? '))
    for i in range(n):
        num = int(input(f"Inserisci numero {i+1}: "))
        numeri.append(num)
    return numeri

# Funzione per il calcolo della media
def mediaNum(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma / len(lista)

# Funzione per trovare e contare i numeri che sono sopra o sotto della media
def numeriSopraSotto(lista, media):
    sopra = 0
    sotto = 0
    for i in lista:
        if i > media:
            sopra += i
        elif i < media:
            sotto += i
    return sopra, sotto

# Funzione per estrarre i numeri maggiori della media
def numeriMaggiori(lista,media):
    numMaggiori = []
    for i in lista:
        if i> media:
            numMaggiori.append(i)
    return numMaggiori

# def numeriCons_uguali(numeri)
numeri = []
lettura = input('Inserisci una lista di numeri: ')
letturaSpezzata = lettura.split()

for i in letturaSpezzata:
    numeri.append(i)

media = mediaNum(numeri)
sopra,sotto = numeriSopraSotto(numeri,media)
Nmaggiori = numeriMaggiori(numeri,media)
# sequenza = numeriCons_uguali(numeri)

print(f"Media dei numeri inseriti: {media}")
print(f"Numeri sopra la media: {sopra}")
print(f"Numeri sotto la media: {sotto}")
print(f"Numeri maggiori della media: {Nmaggiori}")
# print(f"Lunghezza massima di numeri consecutivi uguali: {sequenza}")