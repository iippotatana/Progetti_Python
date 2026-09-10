# Progetti Python - Esercizi Base

Raccolta di script ed esercizi sviluppati per fare pratica con i concetti fondamentali di Python: gestione degli input, strutture di controllo (`if`/`elif`/`else`), cicli (`while`/`for`), collezioni (liste, dizionari) e modularità del codice con funzioni custom.

## Struttura della repository

### Script singoli (radice)
* **`calcolo-iva.py`**: Calcola l'importo dell'IVA e il prezzo finale partendo da prezzo netto e percentuale.
* **`calcolo-sconto.py`**: Applica una percentuale di sconto al superamento di una soglia di spesa.
* **`cassa-negozio.py`**: Simula un registratore di cassa con inserimento iterativo degli articoli e calcolo di sconti progressivi sul totale.
* **`gestione-voti.py`**: Analizzatore base che calcola media, voto massimo, voto minimo e numero di sufficienze da una lista di voti inseriti a terminale.

### `registro_studenti/`
Applicazione CLI modulare per la gestione di un registro scolastico:
* **`funzioni.py`**: Modulo contenente la logica applicativa (aggiunta voti a dizionario, calcolo medie individuali e ricerca dello studente con la media più alta).
* **`main.py`**: Punto di ingresso del programma con menu interattivo a terminale per l'utente.

## Prerequisiti
* Python 3.10+ installato

## Esecuzione

* **Per eseguire uno script singolo:**
  ```bash
  python nome_file.py
  ```
* **Per avviare il registro studenti:**
  ```bash
  cd registro_studenti
  python main.py
  ```

