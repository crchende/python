print("Lucru cu fisiere JSON")

import os, time
import json

#print(dir(time))
d = os.path.curdir
print("Directorul initial:", \
	os.path.realpath(d))

print('Continut director:')
print(os.listdir(d))

'''
print("Schimb directorul:")
os.chdir("CipCode/2_alte_elemente_limbaj_python/lucru_cu_fisiere")
d = os.path.curdir
print(os.path.realpath(d))
print('Continut director:')
print(os.listdir(d))
'''

#print(dir(json))
#print(help(json.load))

print('Transformare directa din fisier in obiecte Python')
with open('fisier1_json.json') as f:
    json_ob = json.load(f)
    
print(json_ob)
print(type(json_ob))

print('Optiune - citesc fisierul si convertesc continutul')
with open('fisier1_json.json') as f:
    txt_json = f.read()
    
print('txt json:\n', txt_json, sep='')

json_ob1 = json.loads(txt_json)
print("Obiect creat din text:", json_ob1)
print(type(json_ob1))


print("Extind dictionarul creat din json.")
json_ob1["nou"] = f"Un nou element {time.ctime()}"
print(json_ob1)

print('Salvare json_ob1 in fisier:')
with open('fisier1_mod.json', 'w') as f:
    json.dump(json_ob1, f)

print('Verificare - incarcare fisier generat:')
with open('fisier1_mod.json') as f:
    json_ob1_1 = json.load(f)
print(json_ob1_1)
