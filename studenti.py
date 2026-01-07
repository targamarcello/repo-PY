"""
Scrivi un programma che gestisca i dati di una classe.
L’utente inserisce per ogni studente: nome e una lista di voti (numeri interi da 1 a 10).
Il programma deve:
● salvare i dati in una lista di liste (o lista di dizionari)
● usare una funzione per calcolare la media dei voti di ogni studente
● usare un ciclo per determinare:
○ lo studente con la media più alta
○ lo studente con la media più bassa
● creare una nuova lista con i nomi degli studenti promossi (media ≥ 6)
● stampare un riepilogo finale con nome, media e stato (promosso / bocciato)
"""


def mediaVoti(voti):
    return sum(voti) / len(voti)


classe = []

n = int(input("Quanti studenti ci sono nella classe ?"))

#Inserimento studenti
for i in range(n):
    nome = input(f"Inserisci nome studente{i+1}: ")
    voti = []
    votiStudente = int(input("Quanti voti ha preso sto soggetto? "))
    for j in range(votiStudente):
        voto = int(input(f"Inserisci voto {j+1} (1-10)"))
        voti.append(voto)

    studente = {"nome": nome, "voti": voti}
    classe.append(studente)

#calcolo media
stud_promossi = []
studMax = None
studMin = None
for stud in classe:
    media = mediaVoti(studente['voti'])
    studente['media'] = media
    if studMax is None or media > studMax['media']:
        studMax = studente
    if studMin is None or media < studMin['media']:
        studMin = studente
    if media >=6:
        stud_promossi.append(studente)

#Riepilogo
print('\n======== RIEPILOGO ========\n')
for stud in classe:
    if stud['media']>=6:
        stato = 'Promosso'
    else:
        stato = 'Bocciato'
    print(f'Nome: {stud["nome"]} - Media: {stud["media"]:.2f} - Stato: {stato}')
    
print(f'\nStudente con la media più alta: {studMax["nome"]} - {studMax["media"]:.2f}')
print(f'\nStudente con la media più bassa: {studMin["nome"]} - {studMin["media"]:.2f}')
print('Studenti promossi: ',stud_promossi)
