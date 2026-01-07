"""
Scrivi un programma che chieda all’utente di inserire una lista di numeri interi.
Usa funzioni e cicli per:
● calcolare la media dei numeri
● contare quanti numeri sono sopra la media e quanti sotto
● creare una nuova lista contenente solo i numeri maggiori della media
● determinare la lunghezza della sequenza più lunga di numeri consecutivi uguali
"""
def leggiNum():
    numeri =[]
    n= int(input('Quanti numeri vuoi inserire? '))
    for i in range(n):
        num = int(input(f"Inserisci numero {i+1}: "))
        numeri.append(num)
    return numeri

def mediaNum(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma / len(lista)


def numeriSopraSotto(lista, media):
    sopra = 0
    sotto = 0
    for i in lista:
        if i > media:
            sopra += i
        elif i < media:
            sotto += i
    return sopra, sotto
# def numeriMaggiori(lista):
