voto = float(input("Inserisci il voto (1-10): "))

lista_voti = []
conta = 0
media = 0
somma = 0
conta_suff = 0

while voto:
    if voto == -1:
        break
    elif voto > 10 or voto < 1:
        print("Hai inserito un valore non valido")
    else:
        conta += 1
        lista_voti.append(voto)

    voto = float(input("Inserisci il voto (1-10): "))

if not lista_voti:
    print("Non è stato inserito alcun voto")
else:
    maggiore = lista_voti[0]
    minore = lista_voti[0]

    for voto in lista_voti:
        somma += voto
        if voto >= 6:
            conta_suff += 1
        if voto > maggiore:
            maggiore = voto
        if voto < minore:
            minore = voto

    media = somma / conta

    print(f"Lista:{lista_voti}")
    print(f"Media:{media}")
    print(f"Maggiore:{maggiore}")
    print(f"Minore:{minore}")
    print(f"Sufficienze:{conta_suff}")

