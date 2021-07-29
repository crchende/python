import subprocess as sp

'''
    Executie comenzi sistem operare si afisare rezultat
        subprocess.getoutput(cmd)
        
    Doar executie - cand nu ne intereseaza outputul:
        subprocess.run(cmd)
'''

print("Calea curenta: sp.getotput('pwd')", sp.getoutput('pwd'))

print("Outputul comenzii ls -la: sp.getoutput('ls -la'): \n", sp.getoutput('ls -la'))

#obs - nu merge sa dau si parametrii pe langa comanda - adica ls -la da eroare
print("Doar executia comenzii ls -la: sp.run('ls')", sp.run('ls'))



