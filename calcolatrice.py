#Calcolatrice in Python con liste - cicli - condizioni
opz = ["Addizione","Sottrazione","Moltiplicazione","Divisione","Esci"]
while True:
    print("======= CALCOLATRICE =======\n")
    #stampa del menù
    for i in range(len(opz)):
        print(f"{i+1}.{opz[i]}")
    scelta = int(input("Scegli operazione: "))
    #Esci
    if scelta == 5:
        print("Fine programma....")
        break
    if scelta<1 or scelta>5:
        print("Scelta invalida....")
    
    numeri = []
    n = int(input("Quanti numeri vuoi inserire? "))
    for i in range(n):
        num = float(input(f"Inserisci numero {i+1}: "))
        numeri.append(num)

    #Addizione
    if scelta == 1:
        risultato = 0
        for n in numeri:
            risultato+=n

    #Sottrazione
    elif scelta == 2:
        risultato = numeri[0]
        for i in range(1,len(numeri)):
            risultato-=numeri[i]
    
    #Moltiplicazione
    elif scelta == 3:
        risultato = 1
        for n in numeri:
            risultato*=n

    #Divisione
    elif scelta == 4:
        risultato = numeri[0]
        err = False
        for n in range(1,len(numeri)):
            if numeri[i]!= 0:
                risultato/=numeri[i]
            else: 
                print("Non è possibile dividere per 0.....")
                err = True

    #Stampa risultato
    if not err:
        print("Risultato: ",risultato)