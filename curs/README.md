# 1. Tipuri de date fundamentale, functii, tratare erori.

## 1.1. Tipuri de date fundamentale
Python pune la dispozitie mai multe tipuri de date cum ar fi:

  - **date numerice**: intregi (`int`), reale (`float`)
      > x = 1
      > y = 2.234

    
  - **sir de caractere (string / str)** (IMUTABIL):
      >   `sir1 = "abcd"`
    
  - **lista (`list`)** (elementele pot fi de diverse tipuri.) (MUTABIL):
      >   lst1 = [1, 2, 'doi', 3]


  - **tuplu (`tuple`)** - un tip de date foarte similar cu lista, cu exceptia faptului ca odata definit, nu i se mai pot modifica elementele (IMUTABIL):
      >   tuplu1 = (1, 2, 'doi', 3)


  - **set (`set`)** - un tip de date folosit pentru a reprezenta o colectie de elemente unice. (MUTABIL):
      >   set1 = {1, 2, 3}


  - **dictionar (`dict`)**: colectie de date in care fiecare element este compus intr-o pereche: 'cheie:' 'valoare'
      >     dict1 = {
      >          'cheie1': 'sir - val 1',
      >          2: 200,
      >          'cheie3': [1, 2, 3],
      >      }

## 1.2. Functii

Functia este o constructie care permite sa dam nume unui bloc de cod. De fiecare date cand este nevoie sa executam acel bloc de cod, in loc sa-l rescriem in program unde avem nevoie de el, apelam functia care contine acel bloc de cod. In Pyton, o functie este un obiect. Sintaxa folosita pentru a defini o functie incepe cu linia:  `def numele_functie(parametrii):`, urmata de corpul functiei pe urmatoarele linii. Liniile care definesc blocul de cod care reprezinta corpul functieie, trebuie indentate. Se considera ca functia s-a incheiat cand indentarea revine la nivelul primei linii - care cuprinde `def`, `nume functie`, `parametrii`.

      > # definire functie:
      > def functie1(x, y):
      >   if x > y:
      >      print('argumente:', x, y)
      >   else
      >      print('Eroare: nu este indeplinita conditia x > y')
      >      
      > # apel functie:
      > functie1(4, 3)
      > argumente: 4, 3  # rezultat apel


## 1.3 Tratare erori

Uneori ne putem astepta ca un anuem apel sa genereze eroare si sa intrerupa functionarea programului. Este recomandat ca in astfel de cazuri sa folosim mecanismul de tratare a erorilor din Python, ca capturam eroarea si sa generam un mesaj de eroare care sa-l ajute pe utilizator sa inteleaga ca nu a folosit corect programul. Tratarea erorilor in Python se face cu ajutorul constructiei `try: ... except ... :` :
    > try:
    >    <cod care poate genera eroare>
    > except Exception as e:
    >    <generare mesaj pentru utilizator>

Exemplu:

    > # functie presispusa la erori care blocheaza programul / genereaza exceptii / crash
    > # cazuri in care apelul acesteia genereaza 'crash':
    > # y = 0
    > # x si/sau y nu sunt numere ci string / dictionar / lista
    > 
    > def imparte(x, y):
    >    return(x / y)
    > 
    > # apelul de genul: imparte(1, 0) sau imparte(5, 'unu') vor duce la 'crash' intreruperea executiei programului
    > tratare erori:
    > try:
    >    rez = imparte(1, 0)
    > except Exception as e:
    >    print(f"Nu s-a putut face impartirea: {e}")
    >    exit()

In loc sa primeasca un mesaj de eroare automat, generat de python, se primeste un mesaj de eroare specific aplicatiei.

    


# 2. Lucru cu fisiere

Programele, in timpul executiei (un proces este un program aflat in executie) folosesc memoria pentru a incarca datele de care au nevoie pentru a le procesa.
Daca dorim sa pastram aceste informatii este necesar sa le salvam pe hard-disc, in fisiere. Daca dorim sa utilizam informatii existente pe hard-disc, trebuie sa putem citi fisiere.
Pentru a salva informatiile pe hard-disc, si pentru a folosi informatii salvate pe hard-disc trebuie sa putem citi / scrie date din/in fisiere.
Python pune la dispozitie functii prin intermediul carora se pot inchide / deschide fisiere, citi / scrie date.

    > f = open(fisier1_txt.txt, 'r+')   # deschidere fisier
    > date = f.read()                   # citire date din fisier
    > print('date:', date)              # afisare date citite
    > f.write("ceva nou")               # scriere noi date in fisier (cursorul de fisier va fi la sfarsit)
    > f.flush()                         # fortam scrierea in fisier, datele sunt tinute intr-un buffer si dupa ce acesta se umple sunt scrise pe hard-disc
    >                                   # flush forteaza scrierea pe hard-disc inainte de umplerea bufferului.
    > f.seek(0)                         # mutare cursor la inceputul fisierului
    > date_noi = f.read()
    > print('date_noi:', date_noi)      # continutul fisierului, inclusiv ce am scris cu write
    > f.close()                         # inchidere fisier
    

# 3. Reprezentarea datelor in mod TEXT cu CSV, JSON, YAML

Serializare datelor - transformarea datelor intr-un sir de octeti care poate fi scris intr-un fisier si care apoi poate fi preluat din fisier si transformat folosit pentru crea datele in memorie.
Modulul 'pickle' din python pune la dispozitie metode de serializare - in forma `binara`.

Metodele de formatare informatie mentionate mai sus, pun la dispozitie un mecanism de serializare a datelor intr-un format lizibil, `text` - usor de citit de operatorul uman - si usor de procesat de catre calculator in vederea transferului de informatii intre programe, salvarii, incarcarii acesteia din fisiere.
Pentru CSV, JSON, YAML, exista module python care contin API-ul / functiile / obiectele prin care se poate interactiona cu datele formatate.

Ca nota generala, modulele `pickle`, `yaml`, `json` au metode similare pentru incarcarea datelor: `load` respectiv formatare si scriere: `dump`.
`load`: citeste datele din fisier le prelucreaza si le transforma in obiecte in memorie.
`dump`: preia obiectele din memorie, le transforma in text / octeti, si le scrie in fisier.

Modulul CSV nu foloseste metodele `load` si `dump` ci `reader` si `writer`.

Schimbul de date intre aplicatii este frecvent. Datele pot fi de diverse tipuri (siruri, liste, dictionare etc.) si in functie de limbajul de programare folosit, vor fi reprezentate in memorie pe mai multi octeti. Modul in care octetii sunt structurati (modul intern de reprezentare) - ce reprezinta primul octet, al doilea etc. -  difera de la un limbaj de programare la altul. Datele afisate in acelasi mod in care sunt reprezentate intern, nu sunt lizibile / este forte greu de intles ce reprezinta. 

Pentru om este usor sa scrie si sa citeasca date in format text. Calculatorul analizeaza usor datele sub forma de text (operatiunea de parsare) in vederea generarii acestora in format intern.

Schimbul de date in mod text este frecvent si intre operatori umani si calculator (nu doar intre aplicatii). Se folosesc frecvent fisiere de configurare pentru a configura modul in care arata si se comporta o aplicatie.

Exemple de utilizare date formatate JSON, YAML, CSV.

Uneltele folosite in DevOps: Jenkins, GitHub, Terraform, Ansible, Kubernetes - folosesc frecvent fisiere in format JSON, YAML.

Aplicatia Excel sau aplicatii similare de calcul tabelar pot salva datele in format CSV sau pot incarca fisiere CSV (text, cu linii si valori pe linii separate cu virgula).

Datele, reprezentate sub format JSON si YAML se mai numesc si date serializate. Prin serializare, se transforma datele din reprezentarea interna (octeti structurati intr-un anume mod) in format text, inteligibil si pentru om si usor de transformat in format intern pentru calculator.

Atat YAML cat si JSON reprezinta un mod de a formata date - de a exprima in mod text siruri, liste, dictionare.

CSV reprezinta un alt mod de formatare, prin care datele dintr-un tabel sunt convertinte in text (si viceversa).
Valorile din celulele de pe o linie se separa prin virgula (sau alt separator)
  
  - CSV:  "Comma-separated values (CSV) is a text file format that uses commas to separate values, and newlines to separate records." - https://en.wikipedia.org/wiki/Comma-separated_values
  - JSON: "JSON (JavaScript Object Notation) is a lightweight data-interchange format" - (https://www.json.org/json-en.html)
  - YAML: "YAML is a human-friendly data serialization language for all programming languages." - (https://yaml.org/)

Exemple de utilizare metodelor de formatare CSV, JSON, YAML - fisierele sunt in acest director:

    > fisier de date             fisier python de prelucrare a datelor
    > ------------------------------------------------------------------
    > fisier1_csv.csv            lucru_cu_csv.py
    > fisier1_yaml.yaml          lucru_cu_yaml.py
    > fisieer1_json.json         lucru_cu_json.py


# Reprezentari schematice ajutatoare de pe LINKEDIN
`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/33ff569c-43a3-440f-b219-fcc0036af67a)

`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/3feec423-fe9d-4fa9-8977-db54485b7554)


`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/229d8bda-b934-43eb-bc24-f8c4f1295ab4)


`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/4ceab77c-84f1-47f2-a935-12aa1f545fe3)


`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/73c0c083-166b-4a33-9030-30178a93c26c)


`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/899809bb-0e31-455d-b68c-2a7c03ffd728)


`[sursa: linkedin]`
![image](https://github.com/crchende/personal/assets/57460107/a9bfa6b4-d6be-4f68-982f-31a0cd5f4163)

