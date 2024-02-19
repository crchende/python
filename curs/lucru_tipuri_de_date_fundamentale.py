sir1 = "exemplu_sir_1"
lst1 = [1, 2, 'doi', 3]
dict1 = {
	    'cheie1': 'valoare1',
	    'materii': ['matematica', 'informatica'],
	    'medie_m': 9,
	    'medie_i': 10
}

#print(dir(sir1)) # dir(str)
#print(dir(lst1))
#print(dir(dict1))

#print(help(str.strip))

print('Verificare tip de date')
print(type(sir1), type(sir1) is str)
print(type(lst1), type(lst1) is list)
print(type(dict1), type(dict1) is dict)

print()
print('Lungime / numar elemente')
print('Lungime sir1:   ', len(sir1))
print('Lungime lista1: ', len(lst1))
print('Lungime dict1:  ', len(dict1))

print()
print('Adaugare elemente:')
sir2 = sir1 + 'X'
print('sir2:', sir2)
print('sir1:', sir1, '(nemodificat)')


lst1.append(5)
print('lst1:', lst1)

dict1['cheie_el_5'] = 'valoare_el_5'
print('dict1:', dict1)

print()
print('Verificare apartenenta:')
print('subsir in sir', 'exe' in sir1)
print('element in lista', 1 in lst1)
print('cheie in dictionar', 'medie_m' in dict1)

print()
print('Accesare element')
print('sir, poz 0:', sir1[0])
print('lst poz 3:', lst1[3])
print('dict, cheie "materii":', dict1['materii'])

print()
print('Accesare plaja elemente / "slicing"')
print('plaja valori - [start, stop) echivalent interval matematic')
print('sir, el 1-3:', sir1[1:4])
print('lst, el 3-4:', lst1[3:5])
#dict1[0:2]
try:
    print('dict, el 0-1:', dict1[0:2])
except Exception as e:
    print('Eroare:', e)
    
print()
print('Parcurgere element cu element')
# functioneaza similar la lista si la sir
# la dictionar se parcurg cheile
for el in lst1:
    print(el)
print()
for k in dict1:
    print(k, dict1[k], sep =': ')

print()    
print('Parcurgere dupa pozitie: "range"')
for i in range(0, len(lst1)):
    print(i, lst1[i], sep=": ")

print()

print('Elementele sirului nu pot fi modificate individual')
print('Sirul de caractere este un tip de date imutabil')
try:
    sir1[0] = 'E'
except Exception as e:
    print('Eroare modificare sir:', e)
    
print('Modificare elemente LISTA:')
print(lst1)
lst1[4] = 500 # lst1[len(lst1)], lst1[-1]
print(lst1)

print('Modificare elemente DICTIONAR:')
print(dict1['cheie_el_5'])
dict1['cheie_el_5'] += '_MOD'
print(dict1['cheie_el_5'])

print()
print('Stergere / inserare elemente. LISTA')
el_0 = lst1.pop(0)
print(el_0, lst1)
lst1.insert(0, el_0)
print(lst1)
u_el = lst1.pop()
print(u_el, lst1)
lst1.append(500)
print(lst1)
el_3 = lst1.pop(2)
print(el_3, lst1)
lst1.insert(2, el_3)
print(lst1)

print()
print('Stergere / inserare elemente. DICTIONAR')
val_k1 = dict1.pop('cheie1')
print(val_k1, dict1)
dict1['cheie1'] = val_k1
print(dir(dict1))


print()
print('Functii de procesare siruri')
print('Modificare capete => sir nou')
sir2 = sir1.strip('e1')
print('sir2:', sir2)
print('sir1:', sir1, '(nemodificat)')

sir2 = sir1.lstrip('e1')
print('sir2:', sir2)
sir2 = sir1.rstrip('e1')
print('sir2:', sir2)

sir2 = sir1.replace('e', 'E')
print(sir2)

# vechi, nou, de cate ori
sir2 = sir1.replace('e', 'E', 1)
print(sir2)

print('Sir - index element')
print('poz primul e:', sir1.index('e'))
print('poz urmatorul e:', sir1.index('e', 1))
print('poz ultimul e:', sir1.rindex('e'))


####################
print()
print("="*10)
print()

print('Conversie SIR -> LISTA')
# str.split str.join
l1_sir1 = sir1.split('_')
print(l1_sir1)
l2_sir1 = list(sir1)
print(l2_sir1)

print('Conversie LISTA -> SIR')
sir_l1 = "--".join(l1_sir1)
print(sir_l1)


####################
print()
print("="*10)
print()
print('func_in')
def func_in(element, colectie):
    for el in colectie:
        if el == element:
            return True    
    return False
    
print(func_in('e', sir1), 'e' in sir1)
print(func_in('ex', sir1), 'ex' in sir1)
print(func_in(2, lst1))
print(func_in(10, lst1))
print(func_in('cheie1', dict1))
print(func_in('cheie10', dict1))

print()
print('func_count')
def func_count(element, colectie):
    nr = 0
    for el in colectie:
        if el == element:
            nr += 1
    return nr

print('nr de "e" in sir1:', sir1.count('e'))
print('func_count', func_count('e', sir1))
