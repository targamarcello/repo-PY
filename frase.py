'''
Analisi di una frase
Scrivi un programma che chieda all’utente di inserire una frase.
Usa liste, cicli e funzioni per:
● separare la frase in una lista di parole
● contare quante volte compare ogni parola
● trovare la parola più lunga e quella più corta
● creare una lista delle parole che compaiono più di una volta
'''

# Funzione che separa la frase in lista di parole
def separaFrase(frase):
    return frase.split()

# Funzione che conta le occorrenze in ogni singola parola
def occorrenze(listaParole):
    occorrenze = {}
    for parola in listaParole:
        if parola in occorrenze:
            occorrenze[parola] +=1
        else:
            occorrenze[parola] = 1
    return occorrenze

# Funzione per trovare la parola più lunga e quella più corta
def lungaCorta(listaParole):
    lunga = listaParole[0]
    corta = listaParole[0]
    for parola in listaParole:
        if len(parola) > len(lunga):
            lunga = parola
        if len(parola) < len(corta):
            corta = parola
    return lunga,corta

# Funzione per trovare le parole che si ripetono
def ripetizioni(occorrenze):
    ripetute = []
    for parola,num in occorrenze.items():
        if num > 1:
            ripetute.append(parola)
        return ripetute

frase = input('Inserire una frase')
frase = frase.lower()

listaParole = separaFrase(frase)
conteggio = occorrenze(listaParole)
pLunga, pCorta = lungaCorta(listaParole)
ripetute = ripetizioni(conteggio)

#Riepilogo
print('\nAnalisi della frase\n')
print(f'Lista di tutte le parole: {listaParole}\n')
print(f'Conteggio delle parole:\n')
for parola,num in conteggio.items():
    print(f'- {parola}: {num}')
print(f'\nParola più lunga: {pLunga}')
print(f'Parola più corta: {pCorta}')
print(f'Parole che si ripetono:')
if ripetute:
    print(ripetute)
else: 
    print('Non ci sono ripetizioni')