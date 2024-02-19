# 1. Elemente de baza. Tipuri de date fundamentale, functii, tratare erori.

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

  

# 2. Lucru cu fisiere

Datele procesate de aplicatii sunt incarcate in memorie. Pentru a salva informatiile pe hard-disc, pentru a folosi informatii salvate pe hard-disc trebuie sa putem citi / scrie date din/in fisiere.
Python pune la dispozitie mai multe functii prin intermediul carora se pot accesa fisiere, citi si scrie date.
    


# 3. Reprezentarea informatiei in format TEXT cu CSV, JSON, YAML

Schimbul de date intre aplicatii este frecvent. Datele pot fi de diverse tipuri (siruri, liste, dictionare etc.) si in functie de limbajul de programare folosit, for fi reprezentate in memorie pe mai multi octeti. Modul in care octetii sunt structurati - ce reprezinta primul octet, al doilea etc, difera de la un limbaj de programare la altul. Modul intern de reprezentare (cum sunt datele in memorie) este neinteligibil de catre un operator uman.
Pentru om este usor sa scrie si sa citeasca date in format text. Pentru calculator este usor de analizat analizat date in mod text (parsare) si sa genereze apoi datele in format intern.
Mai mult, schimbul de date in mod text este frecvent si intre operatori umani si calculator. Se folosesc frecvent fisiere de configurare pentru a configura modul in care arata si se comporta o aplicatie.

Datele, reprezentate sub format JSON si YAML se mai numesc si date serializate. Prin serializare, se transforma datele din reprezentarea interna (octeti structurati intr-un anume mod) in format text, inteligibil si pentru om si usor de transformat in format intern pentru calculator.

Atat YAML cat si JSON reprezinta un mod de a formata date - de a exprima in mod text siruri, liste, dictionare.

CSV reprezinta un alt mod de formatare, prin care datele dintr-un tabel sunt convertinte in text (si viceversa).
Valorile din celulele de pe o linie se separa prin virgula (sau alt separator)
  
  - CSV:  "Comma-separated values (CSV) is a text file format that uses commas to separate values, and newlines to separate records." - https://en.wikipedia.org/wiki/Comma-separated_values
  - JSON: "JSON (JavaScript Object Notation) is a lightweight data-interchange format" - (https://www.json.org/json-en.html)
  - YAML: "YAML is a human-friendly data serialization language for all programming languages." - (https://yaml.org/)


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

