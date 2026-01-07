# commento
'''
commento su più righe e Docstring
'''
# python è un linguaggio interpretato : il codice viene 
# eseguito riga per riga non nella sua interezza (compilatore)
print("ciao") # print() serve per stampare a schermo
print(5+3) # stampo direttamente la somma di due numeri
# variabili: è un contenitore di dati (testi, numeri, caratteri etc..)
# è un nome che fa riferimento a un valore salvato in memoria
'''
NB: Python è un linguaggio NON Tipizzato
es: numero = 18
Come di fa a tipizzare python:
nome_variabile : tipo_di_dato = valore
es: numero: int = 18
tipi di dato principali in python
int -> numeri interi
float -> numeri decimali
str -> stringhe (testi/caratteri)
bool -> True/False

CAST (conversione di tipo di dato)
es: 
x = "10"
y = int(x)
'''
x = "10" # inizialmente è una stringa
y = int(x) # conversione ad intero
print(y + 4) # stampo la somma di 2 interi

# input() serve per leggere quello che viene scritto su console
# NB: Legge SEMPRE una stringa
#nome = input("Come ti chiami: ") # legge la stringa da input
#eta = int(input("Quanti anni hai?: ")) # legge la stringa e la converte in numero
# f-string (format string): si scrive una f davanti a tutto e si mettono
# le variabili all'inerno delle graffe
#print(f"Ciao {nome}, hai {eta} anni")
#print("Ciao", nome, "hai ", eta) # se utilizzo la , per unire le stringhe/numeri
# NON devo fare il casting
# print("Ciao"+ nome + "hai " , int(eta)) # se utilizzo il + per concatenare
# le stringhe devo fare il casting

# NB: stringhe: sono viste come "vettori", che accedo ad ogni carattere 
# attraverso un indice testo[indice] se vado verso destra
# altrimentimenti utilizzo testo[-indice] se vado verso sinistra
# si parte sempre da 0
testo = "Ciao"
print(testo[0])
print(testo[1])
print(testo[2])
print(testo[3])

print(testo[-0])
print(testo[-3])
print(testo[-2])
print(testo[-1])

# estrapolazione della sottostringa
testo2 = "Arianna"
fraseMeta = testo2[0:4] # dal primo indice all'ultimo NON compreso
print(fraseMeta)

# le condizioni
# if condizione:
#   istruzioni if
# else:
#   istruzioni else
numero = 18
if numero < 0:
    print("minore di 0")
else:
    print("maggiore o uguale a 0")

# NON ESISTE lo SWITCH CASE in PYTHON!
# si usa l'elif
if numero < 0:
    print("minore di 0")
elif numero == 0:
    print("uguale a 0")
# tanti elif
else: # mettelo sempre come condizione di default
    print("maggiore di 0")