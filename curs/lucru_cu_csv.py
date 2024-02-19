print("Lucru cu fisiere CSV")

import os
import csv

#print(dir(time))
d = os.path.curdir
print("Directorul initial:", \
	os.path.realpath(d))

print('Continut director:')
print(os.listdir(d))

'''
print("Schimb directorul:")
os.chdir("<cale catre directorul care contine fisierul fisier>")
d = os.path.curdir
print(os.path.realpath(d))
print('Continut director:')
print(os.listdir(d))
'''

print('Metode si atribute csv:')
#print(dir(csv))
#print(help(csv.reader))

# In cazul in care fisierul nu este in directorul in care se ruleaza programu
# trebuie data si calea catre fisier
print('Transformare directa din fisier in obiecte Python')
with open('fisier1_csv.csv') as f:
    csv_generator = csv.reader(f)
    csv_data = list(csv_generator)
    
print(csv_data)

print('Tipul obiectului:', type(csv_data))

print('Optiune - citesc fisierul si convertesc continutul')
txt_csv = []
with open('fisier1_csv.csv') as f:
    #for ln in f:
    #    txt_csv.append(ln)
    # 
    #-echivalent cu-
    #txt_csv = list(f)
    # 
    # alta abordare:
    txt_csv = f.read()
    lst_txt_csv = txt_csv.split('\n')
    
print('txt csv:\n', txt_csv, sep='')
print('lst txt csv:\n', lst_txt_csv, sep='')


#print(help(csv.reader))

csv_ob1 = list(csv.reader(lst_txt_csv))
print("Obiect creat din lst text:\n", csv_ob1)
print(type(csv_ob1))

print("Extind lista creata din csv.")
csv_ob1.append([10, 20, 30])
print("csv_ob1:", csv_ob1)

#print(help(csv.writer))
print('Salvare csv_ob1 in fisier:')
with open('fisier1_mod.csv', 'w') as f:
   csv_w = csv.writer(f)
   #print(dir(csv_w))
   for el in csv_ob1:
       #print(el)
       csv_w.writerow(el)
       
   # echivalent cu:
   #csv_w.writerows(csv_ob1)

print('Verificare - incarcare fisier generat:')
with open('fisier1_mod.csv') as f:
    txt = f.read()
print("text:\n", txt, sep='')   

with open('fisier1_mod.csv') as f:
    #txt = f.read()
    csv_g = csv.reader(f)
    csv_ob1_1 = list(csv_g)
#print("text:\n", txt, end = '')
print("csv_ob1_1:\n", csv_ob1_1, sep='')

#print(help(print))
