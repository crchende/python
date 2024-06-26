`Curs Python`
=========================================================

# Cuprins

1. [Elemente de baza](#elemente-de-baza)
   1. [Tipuri de date fundamentale](#tipuri-de-date-fundamentale)
   1. [Instructiuni de control](#instructiuni-de-control)
   1. [Functii](#functii)
   1. [Tratare erori](tratare-erori)

1. [Lucru cu fisiere](#lucru-cu-fisiere)
1. [Serializarea datelor](#serializarea-datelor)
1. [Programare Orientata Obiect](#programare-orientata-obiect)
1. [Exemplu Aplicatie WEB cu Flask](https://github.com/crchende/sysinfo)
1. [Exemplu utilizare biblioteca pentru trasare grafice - matplotlib](https://github.com/crchende/sysinfo/tree/main/app/grafice)
1. [Reprezentarei schematice ajutatoare de pe LINKEDIN](#reprezentari-schematice-ajutatoare-de-pe-linkedin)
1. [Ghid de pregatire Python](https://docs.google.com/spreadsheets/d/1NDuLDkdwEt3iD7Z7VuLEAnn4gtN9X-gJTuxWxrBPZLE/edit#gid=185047453)

# Elemente de baza
[cuprins](#cuprins)

## Tipuri de date fundamentale
[Exemplu: lucru_tipuri_de_date_fundamentale.py](https://github.com/crchende/python/blob/master/curs/lucru_tipuri_de_date_fundamentale.py)

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

## Instructiuni de control
[cuprins](#cuprins)

  `if ... elif ... else`,
  
  `for element in collection / for i in range(strat, stop, step)`, 
  
  `while`

## Functii
[cuprins](#cuprins)

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


## Tratare erori
[cuprins](#cuprins)

Uneori ne putem astepta ca un apel sa genereze eroare si sa intrerupa functionarea programului. Este recomandat ca in astfel de cazuri sa folosim mecanismul de tratare a erorilor din Python, sa capturam eroarea si sa generam un mesaj de eroare care sa-l ajute pe utilizator sa inteleaga ce s-a intamplat. Tratarea erorilor in Python se face cu ajutorul constructiei `try: ... except ... :` :
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

    


# Lucru cu fisiere
[cuprins](#cuprins)

[Exemplu: citire_scriere_fisier.py](https://github.com/crchende/python/blob/master/curs/citire_scriere_fisier.py:)

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
    

# Serializarea datelor
[cuprins](#cuprins)

si reprezentarea acestora in mod TEXT cu `CSV`, `JSON`, `YAML`

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


# Programare Orientata Obiect
[cuprins](#cuprins)

`POO`
`(Object Oriented Programming / OOP)`

[Exemplu: clase_obiecte_relatii.py](https://github.com/crchende/python/blob/master/curs/clase_obiecte_relatii.py)

Metoda de programare orientata obiect ne pune la dispozitie mijloace prin care putem reprezenta in cod obiecte generate pe baza obiectelor cu care ne intalnim in viata de zi cu zi.
Astfel, putem crea `clase` - tipuri de date complexe - care includ atat proprietati/atribute (variabile) cat si metode (functii) 

(Ne putem gandi la clase ca la o extensie a structurilor din C, care pe langa variabile de diverse tipuri pot include si functii)

Un `obiect` este o instanta a unei `clase`. 

Un alt mod de a exprima acelasi lucru este: o variabila de tip clasa este un obiect.

Exemplu:

   > `CLASA`
   > `Masina`
   >    - putem asocia notiunea de masina cu o clasa. Cand spunem masina intelegem ceva complex - roti, motor, caroserie, etc
   >    - este ceva abstract / generic
   >
   > `OBIECT` 
   > `masina_mea`
   >    - este un obiect de tip masina
   >    - este masina ea, stiu care este, pot sa o conduc etc
   >
   > INSTANTIERE / creare variabila de tip clasa in Python
   >    - `masina_mea = Masina(culoare='verde', combustibil='gaz', putere='100KW')`
   >    - apelul creaza obiectul masina_mea configureaza proprietatile specificate in apel.


### Notiuni de baza referitoare la programarea orientata obiect:

   - `Clasa`:               Tip de date care poate contine atat atribute/proprieteati (variabile) cat si metode (functii)
     
   - `Obiect`:              O instanta a unei clase / o variabila de tip clasa

   `Cei patru piloni ai POO`
     
   - `Abstractizare`        Cand modelam obiectul ne referim la latura care ne intereseaza, de exemplu pentru o aplicatie 'car sharing' ne vor interesa mai mult detalii de utilizare si partajare a masinii.
                              pentru o aplicatie de reparatii / proiectare, ne vor interesa mai mult detalii tehnice si mai putin detalii de folosire a masinii in regim 'car sharing'.
     
   - `Mostenire`:           Pentru reutilizarea codului, clasele pot fi organizate in ierarhii de clase de baza (clase parinte) si clase derivate (clase copil). Clasele copil mostenesc proprietatile si metodele
                              claselor parinte.
     
   - `Polimorfism`              'mai multe forme' - clasele copil pot suprascrie proprietati si metode ale claselor parinte. Desi au aceeasi forma (nume in acest caz), valoarea, functionalitatea metodei este diferita
                              intre parinte si copil.
     
   - `Incapsulare`              Informatiile interene ale clasei / obiectului nu sunt vizibile in exterior (de ex, nu putem accesa direct, ca utilizatori, un anume surub din cutia de viteze)
                              Metodele si proprietatile claselor pot fi clasificate in `publice`, `_protejate` si `__private` (caracterul variabilei este stabilit de prefixul _ sau __). 
                              Cele publice sunt accesibile din exterior. Cele private nu. 
                              In Python accesul nu este atat de strict ca in alte limbaje. Variabilele _protejate pot fi accesate direct. Cele __private nu pot fi accesate direct dar pot fi accesate prin
                              prefixarea acestora cu _Clasa__variabila.
     

   ### Relatii intre clase

   - `MOSTENIRE`: `is a` / `este un/o`: Ex: clasa de masini `Dacia` este o `Masina`
     
   - `COMPUNERE`:  `has a` / `are un/o`: Ex: `Masina` are un `Motor` (dar nu este un motor)



# Reprezentari schematice ajutatoare de pe LINKEDIN
[cuprins](#cuprins)


`[sursa: linkedin]`

![linkedin_tipuri_date](https://github.com/crchende/python/assets/57460107/d3f6dbdc-3ddb-4d54-8684-4d7f310cb9ac)


`[sursa: linkedin]`

![linkedin_structuri_date2](https://github.com/crchende/python/assets/57460107/ad920dec-3ce5-43ad-b449-02ced8c3e6f1)


`[sursa: linkedin]`

![linkedin_structuri_date1](https://github.com/crchende/python/assets/57460107/23d4b347-6544-47a8-91e8-a565f3c805f4)


`[sursa: linkedin]`

![linkedin_python_cheat_sheet](https://github.com/crchende/python/assets/57460107/d4b0fbcb-b117-4394-bb60-cf9e9e01ab95)


`[sursa: linkedin]`

![linkedin_mindmap_learn_py](https://github.com/crchende/python/assets/57460107/bdb5953e-97e6-46a3-b676-085532101d02)


`[sursa: linkedin]`

![linkedin25_algoritmi](https://github.com/crchende/python/assets/57460107/86b929a8-f5dd-4f9e-b03e-ade6f87b2fb2)


`[sursa: linkedin]`

![linkedin_python_roadmap_for_success](https://github.com/crchende/python/assets/57460107/d058e098-aa88-400d-9c86-25ff0ba46230)
