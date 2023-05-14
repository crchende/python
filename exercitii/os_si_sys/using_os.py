import os

print("\n\n Modul cu functii pentru interactiunea cu sistemul de operare")
print('''
- cale curenta
- cale absoluta
- listare fisiere, directoare
- verificare daca un element este director, fisier 
etc.
''')

#######################################
print("os.path.curdir: ", os.path.curdir)
print("os.path.abspath: ", os.path.abspath(os.path.curdir))

###
cale = os.path.abspath(os.path.curdir)
print("Verific daca exista o cale:", cale , " os.path.exists(cale): ", os.path.exists(cale))
cale = os.path.join(cale, "NU_EXISTA")
print("Verific daca exista o cale:", cale , " os.path.exists(cale): ", os.path.exists(cale))

#######################################
os.chdir("../")
print("Schimbare director: os,chdir(../), os.path.abspath: ", os.path.abspath("."))

#######################################
print("Parcurgere recursiva a unui director - echivalent oarecum cu ls -laR")
gen_dir_walk = os.walk(".")
print("generator walk dir:", gen_dir_walk)

for x in gen_dir_walk:
    print("\ncontinut director:", x, "")
    print(" - Cale: ", x[0])
    print(" - Dir - list: ", x[1])
    print(" - Fisiere - list: ", x[1])

print("\n\nA doua parcurgere a generatorului:")
for x in gen_dir_walk:
    print("continut director:", x, "\n\n")
    
################################################ 
print("Listare continut director si verificare fisier sau director")
print("os.path.listdir('.'): ", os.listdir('.'))
for el in os.listdir("."):
    if os.path.isdir(el):
        print(" - dir:  ", el)
    elif os.path.isfile(el):
        print(" - file: ", el)
       
############################################### 
print("Utilizare os.path.join pentru a forma calea catre un fisier")
cur_abs_path = os.path.abspath('.')
print("Absolute current path: ", cur_abs_path)
for el in os.listdir('.'):
    print("Elementele din directorul curent, cu cale absoluta:", os.path.join(cur_abs_path, el))




