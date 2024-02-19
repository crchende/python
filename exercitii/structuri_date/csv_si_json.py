# Exemplu preluare date in format:
#  - CSV  (comma-separated values) 
#  - JSON
# si adaugare a acestor intr-un dictionar
#
# Citire a datelor din fisier.
# Scriere in fisier in formatele de mai sus.
#
# cip_chende@yahoo.com

import csv
import json


##############
# CSV -> dictionar
# documentatie: https://realpython.com/python-csv/
# 
# Exemplele de mai jos prezinta doar citirea din CSV.
#
# DE STUDIAT de la link-ul indicat:
#  1) scriere date sub forma CSV in fisier cu obiect de tip csv.writer
#
#    with open('new_csv_file.csv', mode='w') as out_csv_f:
#        csv_writer = csv.writer(out_csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#        csv_writer.writerow(<lista cu elementele de pe o linie>)
#  
#  2) scriere unui dictionar intr-un fisier csv folosind obiect de tip csv.DictWriter
#
#  3) folosire librarie 'panda' care pune la dispozitie unelete pentru 'data analytics'
#
#    
##############
# voi pune in acest dictionar materiile si notele
dict_medii = {}
dict_medii['elevi'] = []; # vom salva numele elevilor intr-o lista sa fie mai usor de gasit

# Citirea din fisierele csv se face prin intermediul unor obiecte 'reader'
# 
# csv.reader(file_id, delimiter = ',', quotechar = '"', escapechar = ')
#  - genereaza o lista pentru fiecare linie din fisier, cu elemente portiunile 
#    de text separate prin 'delimiter' - default: ','
#    In cazul in care avem in text virgule care nu vrem sa fie considerate separatori,
#    Textul respectiv ar trebui sa fie incadrat intre caractere 'quotechar' - default: '"',
#    sau virgulele ar trebui sa fie precedate de caracerul 'escapechar'. Nu are valoare default.
#
#
#
##############
# citire cu 'csv.reader'
# si adaugare 'de mana' in dictionarul dict_medii
#
# TBD - tratare erori - daca am mai multe sau mai putine elemente pe o linie
##############
#
# Folosesc managerul de context 'with' cand citesc datele din fisier.
# Acesta se asigura ca dupa folosirea fisierului, cand se iese din 'width'
# fisierul va fi inchis.
#
with open('note_csv.txt', mode = 'r') as csv_f_id:
    csv_reader = csv.reader(csv_f_id, delimiter=',')
    i = 0
    for row in csv_reader:
        if i == 0: # doar un exemplu, nu afisam mesaj de debug pentru toate liniile
            print("DBG: linie din CSV citita cu csv.reader:", row)
            
        data_type = row[0]
        
    cheia dictionarului este tipul de date adica 'Materii' sau nume elev
    continutul dictionarului este fie lista de materii, fie lista de note
        
        if data_type != "Nume Prenume":
        liniile cu notele pentru fiecare elev
            
        vreau sa am o lista cu elevii
            dict_medii['elevi'].append(data_type)
            
        pentru fiecare elev adaug o intrare in dictionar:
        cheie   - nume elev
        valoare - lista cu medii 
        folosim list comprehension pentru a genera o noua lista
            dict_medii[data_type] = [x.strip() for x in row[1:]]
            
        else:
            #prima linie = contine materiile
            dict_medii["Materii"] = [x.strip() for x in row[1:]]
        i += 1

# Afisare dictionar
i = 1
for k in dict_medii:
folosire f-string - formatare 'inline'
echivalent cu:
"{:3} {:20} {}".format(i, k, dict_medii[k])
    print(f'{i:3} {k:20} {dict_medii[k]}')
    i += 1

###############
# Citire cu csv.DictReader
#
# DictReader pune datele direct intr-un dictionar.
# Cheile vor fi numele coloanelor
# Pentru fiecare linie vom avea linie[nume_coloana] = valoare
#
# Pentru ca avem spatii in fisierul csv, cheile si valorile vor contine extra spatii
# Pentru un fisier CSV cum este generat in mod standard - fara extra spatii
# DictReader poate fi folosit fara probleme.
#
###############
# fisierul a fost inchis la iesirea din 'with' -ul de mai sus, trebuie redeschis
lst_dict_linii = []
with open('note_csv.txt', mode='r') as csv_f_id:
    csv_dict_reader = csv.DictReader(csv_f_id, delimiter = ',')

    print("DBG: csv_dict_reader:", csv_dict_reader)
    
    i = 0
fiecare linie este un dictionar, avand chei, numele din prima linie din CSV
    for row in csv_dict_reader:
        if i == 0: # i poate fi oricare, join in acest caz ia cheile din dictionar
            cap_tabel = " ".join(row)
            print("DBG: cap tabel:", cap_tabel)
            print(f'linie {i}: {row}')
  
    cheile dictionarului si valorile contin spatii ...
    DictReader
        #print("DBG: Linie citita cu DictReader: ", row)
        #print("DBG: Dictionar pe linie: ", row)
        
    Salvez liniile intr-o lista pentru putea utiliza informatia in afara blocului 'with'
    Vom avea o lista de dictionare, fiecare dictionar cu aceleasi chei - prima linie din fisierul csv
        lst_dict_linii.append(row)
        i += 1

# Eroare la rularea codului de mai jos. 
# csv_dict_reader, nu poate fi parcurs in afara blocului 'with'
#
# TBD - de studiat de ce nu se poate face acest lucru
#       sugestie: utilizare generator pentru citire fisier linie cu linie
#
#     - consecinta - dictinarul rezultat nu ramane salvat ... 
#
'''
print(csv_dict_reader)
for row in csv_dict_reader:
cheile dictionarului si valorile contin spatii ...
DictReader
    #print("DBG: Linie citita cu DictReader: ", row)
    for k in row:
        print(f'"{k:30}" -> {row[k]}')
'''

# pot utiliza datele salvate in lst_dict_linii
print("DBG: lst_dict_linii[0]: ", lst_dict_linii[0])
    
    
    
###############
# JSON - nu mai trebuie parcurs linie cu linie ca la CSV
# 
# despre json + exemple
# https://json.org/example.html
#
# Python JSON:
# https://docs.python.org/3/library/json.html
#
###############

# A) citire date din fisier json - cu json.load
f_id = open("note_json.json", mode = 'r')
dict_from_json = json.load(f_id)
f_id.close(); #inchidem fisierul

print("DBG: dict_from_json: ", dict_from_json)

# B) sir json
# putem avea datele si intr-o variabila sub forma de string json
# transformarea sirului json in dictionar se face cu: json.loads(<sir json>)

# C) Conversie dictionar in sir json si scriere in fisier
f_id = open("new_note_json.json", mode = 'w')
f_id.write("\n# salvat in fisier cu json.dump(dictionary_var) - linia aceasta nu respecta sintaxa json. Trebuie stearsa pentru a pute incarca fisierul ca json:\n")
json_from_dict = json.dump(dict_from_json, f_id)
# dump se ocupa si de scriea in fisier
f_id.close()

# D) json.dumps - va scrie intr-un sir, nu intr-un fisier
#    sirul poate fi scris in fisier cu f_id.write(sir)

