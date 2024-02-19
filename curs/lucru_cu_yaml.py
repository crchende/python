print("Lucru cu fisiere YAML")

import os
import yaml

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

#print(dir(yaml))
#print(help(yaml.load))
print('Transformare directa din fisier in obiecte Python')
with open('fisier1_yaml.yaml') as f:
    yaml_ob = yaml.load(f, yaml.Loader)
    
print(yaml_ob)
print(type(yaml_ob))

print('Optiune - citesc fisierul si convertesc continutul')
with open('fisier1_yaml.yaml') as f:
    txt_yaml = f.read()
    
print('txt yaml:\n', txt_yaml, sep='')

#print(dir(yaml))
yaml_ob1 = yaml.load(txt_yaml, yaml.Loader)
print(yaml_ob1)

yaml_ob1.append("element nou")
print(yaml_ob1)
#print(dir(yaml))

print('Salvare yaml_ob1 in fisier:')
with open('fisier1_mod.yaml', 'w') as f:
    yaml.dump(yaml_ob1, f)

print('Verificare - incarcare fisier generat:')
with open('fisier1_mod.yaml') as f:
    yaml_ob1_1 = yaml.load(f, yaml.Loader)
print(yaml_ob1_1)
