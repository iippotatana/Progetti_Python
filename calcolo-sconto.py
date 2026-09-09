spesa = float(input("Inserisci l'importo totale della spesa: "))

if spesa > 50:
    sconto = 10 / 100
    prezzo_sconto = spesa * sconto
    tot = spesa - prezzo_sconto
else:
    sconto = 0
    prezzo_sconto = spesa * sconto
    tot = spesa

print(f"Lo sconto applicato è pari a {prezzo_sconto} euro il totale è di {tot} euro")
