
def aggiungi_voto(registro:dict, nome:str, voto:float):
    """aggiunge il voto alla lista dello studente.
    Se lo studente non esiste ancora nel dizionario,
    lo crea con una nuova lista contenente quel voto."""
    if nome not in registro:
        registro[nome] = []
    registro[nome].append(voto)

def calcola_media_studente(voti:list)->float:
    """riceve una lista di voti e restituisce la media (decimale).
    Se la lista è vuota, restituisce 0"""
    if not voti:
        return 0
    else:
        media = sum(voti) / len(voti)
        return media

def trova_migliore(registro:dict) -> tuple[str|None, float|int]:
    """restituisce il nome dello studente con la media più alta e il rispettivo valore di media."""
    studente_migliore = None
    media_migliore = 0
    for studente,voti in registro.items():
        media_corrente = calcola_media_studente(voti)
        if media_corrente > media_migliore:
            media_migliore = media_corrente
            studente_migliore = studente
    return studente_migliore, media_migliore



