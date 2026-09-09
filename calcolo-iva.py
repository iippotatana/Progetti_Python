netto = float(input("Inserisci il prezzo netto: "))

iva = int(input("Inserisci la percentuale dell'IVA da applicare: "))

prezzo_iva = netto * (iva / 100)

prezzo_tot = netto + prezzo_iva

print(f"Il prezzo finale è di: {prezzo_tot} euro dei quali di iva: {prezzo_iva} euro")
