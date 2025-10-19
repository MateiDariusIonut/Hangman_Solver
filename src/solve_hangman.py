#Citeste fisierul cu dictionarul si creeaza o lista cu cuvintele din el
with open("../data/resource.txt", "r", encoding="utf-8") as f:
    dictionar = [cuvant.strip().upper() for cuvant in f]

#Citeste fisierul de test cu datele cuvintelor
with open("../data/test.csv", "r", encoding="utf-8") as f:
    linii = f.readlines()

'''
Functie care gaseste candidati in dictionar care respecta
pattern-ul cuvantului actual
'''
def gaseste_candidati(pattern, dictionar):

    lungime = len(pattern)
    candidati = []
    for cuvant in dictionar:
        #Sare peste cuvintele care nu au aceeasi lungime cu patternul
        if len(cuvant) != lungime:
            continue
        potrivit = True
        #Verifica daca literele existente in pattern se regasesc si in candidat pe aceleasi pozitii
        for i, lit in enumerate(pattern):
            if lit != '*' and cuvant[i] != lit:
                potrivit = False
                break
        #Daca a gasit un candidat potrivit il adauga in lista de candidati
        if potrivit:
            candidati.append(cuvant)
    return candidati

'''
Functie care gaseste urmatoarea litera de incercat din cuvintele candidate
Aceasta cauta litere in pozitii necunoscute notate cu *, care nu au fost incercate inca
'''
def litera_urmatoare(candidati, pattern, incercate):

    litere_posibile = []

    #Colecteaza toate literele posibile din pozitiile necunoscute ale cuvintelor candidate
    for cuvant in candidati:
        for i, litera in enumerate(cuvant):
            #Ia in considerare doar literele din candidati care se afla pe pozitii necunoscute (*) in pattern
            if pattern[i] == '*':
                litere_posibile.append(litera)

    #Returneaza prima litera care nu a fost incercata inca
    for litera in litere_posibile:
        if litera not in incercate:
            return litera

    return None

total_incercari = 0
#Lista cu frecventa literelor in limba romana
frecventa_litere = ['e', 'a', 'i', 'r', 't', 'n', 'u', 'o', 's', 'c', 'l', 'd', 'm', 'p', 'v', 'b', 'f', 'g', 'h', 'z', 'ă', 'ș', 'ț', 'â', 'î', 'j', 'k', 'w', 'x', 'y', 'q']
rezultate = []
erori = []

#Parcurge fiecare linie din fisierul de intrare
for linie in linii:
    #Imparte linia in componente: ID, pattern, cuvant tinta separate prin ";"
    parti = linie.strip().split(";")

    if len(parti) < 3:
        erori.append(f"Linie invalidă: {linie.strip()}")
        continue

    id_joc = parti[0]   #ID-ul cuvantului
    pattern_curent = list(parti[1].upper())     #Transforma cuvantul care trebuie ghicit intr-o lista pentru manipulare mai usoara
    cuvant = parti[2].upper()       #Cuvantul corect care trebuie ghicit
    incercari_cuv = 0       #Numarul de incercari pentru cuvantul curent
    litere_incercate = []       #Lista cu literele incercate pentru cuvantul curent

    #Validarea datelor
    if not id_joc or not pattern_curent or not cuvant:
        erori.append(f"Lipsă câmpuri în linia: {linie.strip()}")
        continue
    if len(pattern_curent) != len(cuvant):
        erori.append(f"Lungime diferită între pattern si cuvant: {linie.strip()}")
        continue

    #Jocul continua pana cand toate literele sunt ghicite (nu mai exista *)
    while '*' in pattern_curent:

        candidati = gaseste_candidati(pattern_curent, dictionar)    #Gaseste cuvintele care se potrivesc cu pattern-ul curent
        lit = litera_urmatoare(candidati, pattern_curent, litere_incercate)     #Alege urmatoarea litera de incercat

        #Daca nu exista candidati, foloseste frecventa literelor din limba romana
        if not candidati:
            for litera in frecventa_litere:
                if litera.upper() not in litere_incercate:
                    lit = litera.upper()
                    break
        else:
            #Daca exista candidati, dar nu s-a gasit o litera buna, foloseste frecventa literelor
            lit = litera_urmatoare(candidati, pattern_curent, litere_incercate)
            if not lit:
                for litera in frecventa_litere:
                    if litera.upper() not in litere_incercate:
                        lit = litera.upper()
                        break

        #Adauga litera la lista de litere incercate si incrementeaza contorul
        litere_incercate.append(lit)
        incercari_cuv += 1

        #Actualizeaza pattern-ul cu noile litere gasite
        for i, caracter in enumerate(cuvant):
            if caracter == lit:
                pattern_curent[i] = lit

    total_incercari += incercari_cuv
    cuvant_gasit = "".join(pattern_curent) # Converteste pattern-ul inapoi in string

    #Actualizeaza statusul
    if cuvant_gasit == cuvant:
        status = "OK"
    else:
        status = "FAIL"

    #Adauga rezultatul la lista de rezultate
    rezultate.append(f"{id_joc}. Număr încercări: {incercari_cuv}, Cuvânt găsit: {cuvant_gasit}, Status: {status}, Litere încercate: {' '.join(litere_incercate)}")

#Scrie rezultatele in fisierul de iesire
with open("../results/out.csv", "w", encoding="utf-8") as f:
    for linie in rezultate:
        f.write(linie + "\n")
    f.write(f"\nTotal pași: {total_incercari}")

#Scrie erorile in fiserul pentru erori daca acestea exista, daca nu afiseaza un mesaj de confirmare
with open("../results/errors.csv", "w", encoding="utf-8") as f:
    if erori:
        for eroare in erori:
            f.write(eroare + '\n')
    else:
        f.write("Nu s-au găsit erori!")