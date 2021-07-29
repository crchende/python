import sys

print("Cateva functii utile din modulul SYS")
print("\n\n !!! Modulul SYS contine functii si variabile referitoare la interpretor\n\n")
print("sys.version:", sys.version)
print("sys.version.split(' '): ", sys.version.split(' '))

print("sys.version_info:", sys.version_info)
print(f'sys.version_info.major: {sys.version_info.major}, sys.version_info.minor: {sys.version_info.minor}')

print('Calea folosita Python. De unde incarca librarii etc: sys.path:', sys.path)
