
import funzioni as f

registro = {}

scelta = -1

while scelta != 0:
    print("\nMenu:")
    print("1 - Inserisci nome e voto")
    print("2 - Mostra media studenti")
    print("3 - Mostra studente migliore")
    print("0 - Esci")

    scelta = int(input("Seleziona un opzione: "))
    if scelta == 0:
        print("Spegnimento in corso...")
    elif scelta == 1:
        nome = input("Inserisci il nome dello studente: ")
        voto = float(input("Inserisci il voto:"))
        if 1 <= voto <=10:
            f.aggiungi_voto(registro,nome,voto)
        else:
            print("Hai inserito un valore non valido!")

    elif scelta == 2:
        if not registro:
            print("Il registro è vuoto!")
        else:
            for studente, voti in registro.items():
                media = f.calcola_media_studente(voti)
                print(studente, media)

    elif scelta == 3:
        if not registro:
            print("Il registro è vuoto!")
        else:
            migliore, media = f.trova_migliore(registro)
            print(f"Lo studente migliore è: {migliore}, con una media di: {media}")
    else:
        print("Opzione inesistente!")

