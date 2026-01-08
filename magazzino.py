'''
Gestione magazzino
Scrivi un programma che gestisca un magazzino di prodotti.
Ogni prodotto è descritto da: nome, prezzo e quantità disponibile.
Il programma deve:
● salvare i prodotti in una lista di dizionari (o liste)
● usare una funzione per calcolare il valore totale del magazzino
● usare un ciclo per trovare il prodotto con il valore totale più alto (prezzo × quantità)
● creare una lista dei prodotti esauriti (quantità = 0)
● stampare un riepilogo finale
'''
# lista dei prodotti
magazzino = [
    {'nome':'Laptop','prezzo':1000,'quantità':6},
    {'nome':'Mouse','prezzo':50,'quantità':2},
    {'nome':'Tastiera','prezzo':130,'quantità':9},
    {'nome':'Monitor','prezzo':310,'quantità':1},
    {'nome':'Cuffie','prezzo':70,'quantità':0}
]

# Funzione per falcolare il valore contenuto nel magazzino
def valoreMagazzino(prodotti):
    totale = 0
    for prod in prodotti:
        totale += prod['prezzo']*prod['quantità']
    return totale

# Funzione che trova il prodotto più costoso
prodottoCostoso = None
valoreMax = 0
for prod in magazzino:
    valore = prod['prezzo']*prod['quantità']
    if valore > valoreMax:
        valoreMax = valore
        prodottoCostoso = prod
  
# Creazione lista di prodotti esauriti
prodottiEsauriti = []
for prod in magazzino:
    if prod['quantità'] == 0:
        prodottiEsauriti.append(prod)

# Riepilogo
print('\n====== Magazzino ======\n')
print(f'Valore totale del magazzino: {valoreMagazzino(magazzino)}€')
print(f"Prodotto con prezzo più alto:\n{prodottoCostoso['nome']} ({valoreMax})€")
print("\nProdotti esauriti nel magazzino:")
if prodottiEsauriti:
    for prod in prodottiEsauriti:
        print(f"- {prod['nome']}")
else:
    print("Nessun prodotto esaurito")