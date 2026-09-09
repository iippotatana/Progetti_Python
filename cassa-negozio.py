prezzo_articolo = float(input("\nInserisci il prezzo dell' articolo: "))

somma = 0
percentuale = 0
contatore = 0


while prezzo_articolo:

    if prezzo_articolo > 0:
        somma += prezzo_articolo
        contatore += 1
    else:
        print("\nHai inserito un numero negativo!")
    prezzo_articolo = float(input("\nInserisci il prezzo dell' articolo: "))



if somma == 0:
    print("\nNon ce nulla da sommare!")
else:

    if 50 < somma <= 100:
        percentuale = 10 / 100
    elif somma > 100:
        percentuale = 20 / 100

    sconto = somma * percentuale
    totale = somma - sconto

    print(f"\nTotale articoli acquistati: {contatore}")
    print(f"\nTotale lordo: {somma}")
    print(f"\nSconto applicato: {sconto}")
    print(f"\nTotale netto: {totale}")


