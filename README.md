# **Proiect Hangman Solver**

Acest proiect este un solver automat pentru jocul Hangman (Spânzurătoarea) care folosește strategii inteligente pentru găsirea cuvântului din cât mai puțini pași.

## **Tehnologii folosite**
- **Python 3**
- **Encoding UTF-8 pentru suportul diacriticelor**
- **Fișiere CSV**

## **Cum functionează?**
1. Parcurge fișierul cu datele de intrare.
2. Pentru fiecare cuvânt care trebuie ghicit selectează candidații posibili.
3. Din lista de candidați selectează literele care nu au fost încercate și o incearcă pe prima.
4. Dacă s-a găsit o literă bună se actualizează lista de candidați.
5. Se repetă procedeul până când cuvântul este identificat.

## **Structura proiectului**

```bash
Hangman_Solver/
├── data/
│   ├── resource.txt          # Dicționarul de cuvinte românești
│   └── test.csv              # Fișierul de intrare cu cuvintele
├── docs/                     # Documentație suplimentară
├── results/
│   ├── errors.csv            # Erorile găsite în fișierul test.csv
│   └── out.csv               # Rezultate
└── src/
    └── solve_hangman.py      # Scriptul principal care rezolvă jocul Hangman
```

## **Instrucțiuni rulare**

1. **Descărcați folderul cu proiectul**
2. **Deschideți proiectul în PyCharm**
3. **Accesați scriptul solve_hangman.py**
4. **Click pe butonul verde de rulare din partea de sus***

- **Alternativă**
1. **Descărcați folderul cu proiectul**
2. **Deschideți proiectul în PyCharm**
3. **Deschideți terminalul din PyCharm și introduceți comenzile:
```bash
cd src
python solve_hangman.py
```

## **Format intrare/ieșire**

- **Input**
  ```bash
  1;******RA**;ICONOGRAFĂ
  2;*A**C****;FAGOCITUL
  3;*P*C******;APICOLILOR
  ```
- **Output**
  ```bash
  1. Număr încercări: 10, Cuvânt găsit: ICONOGRAFĂ, Status: OK, Litere încercate: A B E N C I O G F Ă
  2. Număr încercări: 12, Cuvânt găsit: FAGOCITUL, Status: OK, Litere încercate: B S A O R H I F G T U L
  3. Număr încercări: 5, Cuvânt găsit: APICOLILOR, Status: OK, Litere încercate: A I O L R
  ```

## **Limitări**
**Pentru ca algoritmul să fie cât mai eficient și să găsească cuvântul căutat din cât mai puține încercări este nevoie ca acesta să se afle în fișierul resource.txt, altfel algoritmul v-a propune litere după frecvența lor, ceea ce poate duce la un număr mai mare de pași.**
