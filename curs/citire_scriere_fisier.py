import os, sys
import time as t

print("Python version: ", sys.version[0:5])
#print(dir(t))


print("Directorul initial:")
d = os.path.curdir
print(os.path.realpath(d))

print(os.listdir(d))

'''
print("Schimb directorul, locatia cu fisierul text:")
os.chdir("<cale catre director>")
d = os.path.curdir
print(os.path.realpath(d))
'''

print("Citire date din fisier. open, read, close")
f = open("fisier1_txt.txt")
data = f.read()
f.close()
print("Am inchis fisierul")
print('Datele citite din fisier:\n', data)

print("Incerc sa citesc din fisierul inchis")
try:
    f.read()
except Exception as e:
    print('Eroare citire din fisier inchis:', e)

print("Citesc din nou din fisier")
print("folosind 'context manager': with")
print('Metoda recomandata!')
print('Citesc tot fisierul')
with open("fisier1_txt.txt") as f:
    d = f.read()
    print(d)

# la iesirea din with, fisierul este 
# inchis automat
print('Verific ca fisierul este inchis',\
	f.closed)

print("Citesc din nou din fisier")
print("linie cu linie cu un bloc de cod  'with'")
print('Metoda recomandata!')
print('Citesc linie cu linie')
with open("fisier1_txt.txt") as f:
    for l in f:
        # liniile contin deja '\n'
        print(l, end='')

print("Scriere si citire")
f = open("fisier1_txt.txt", mode='a+')
f.write(f'Adaugare linie {t.ctime()}\n')
f.flush()
print("Adaugare cu print", file=f, flush=True)
print("Continut fisier modificat")
f.seek(0)
d = f.read()
#print(dir(f))
#print(help(f.seek))
print(d)
f.close()
