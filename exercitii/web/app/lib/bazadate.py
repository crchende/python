'''
Exemplu de biblioteca pentru lucru cu baze de date sqlite, folosind 
API-ul sqlite3.
Baza de date creata va contine un singur tabel: nume_si_salut.
Totul este integrat in clasa DBNumeSiSalut
Pe langa functiile: conectare, inserare date, citire date din tabel, deconectare,
functia initializeaza_baza_de_date, va initializa baza de date daca nu exista.
Ce inseamna initializare:
 - creare baza de date
 - creare tabel
 - adaugare set de date initiale in tabel
Daca baza de date exista o va crea, va crea tabelul si va adauga datele intabel.
Daca tabelul este gol, va adauga setul initial de date in tabel.

Resetarea manuala a bazei de date:
 - se sterge fisierul cu baza de date (numele implicit este db.sqlite)
   daca ati folosit alt nume in aplicatie, stergeti acel fisier.
   Pentru a identifica usor baza de date este recomandat sa aiba extensia '.sqlite'
   Repository-ul este configurat sa ignore fisierele cu aceasta extensie.
'''

import os
if __name__ == "__main__":
    from baza_date_sqlite import BDSqlite
else:
    from lib.baza_date_sqlite import BDSqlite

class BDNumeSiSalut(BDSqlite):
    # implicit, baza de date va fi creata in memorie
    def __init__(self, nume_baza_date="bd.sqlite"):
        self.nume_bd = nume_baza_date

        self.date_initiale = (
            ("nume_si_salut", ("George", "Salut!")),
            ("nume_si_salut", ("John", "Hello!")),
            ("nume_si_salut", ("Giovani", "Ciao!")),
            ("nume_si_salut", ("Ion", "Buna ziua!"))
        )

    ###########################################################
    # Metode specializate pe aceasta baza de date
    ###########################################################
    def selecteaza_nume_si_salut(self):
        sql_q = "SELECT * FROM nume_si_salut"
        return self.selecteaza_date(sql_q)

    def initializeaza_baza_de_date(self):
        '''
            Initializare baza de date dupa crearea acesteia
            Functia nu va adauga tabele daca acestea exista si nici date daca
            tabelele existente contin date.
        '''

        self.creaza_tabel("nume_si_salut", "nume", "salut")
        date_tabel = self.selecteaza_date("SELECT * from nume_si_salut")
        if len(date_tabel) == 0:
            print("DBG: Baza de date trebuie initializata")
            for el in self.date_initiale:
                self.insereaza_in_tabel(el[0], *el[1])

        else:
            print("DBG: nu se mai adauga date, tabelul are deja date")


print("__name__:", __name__)
if __name__ == "__main__":
    #
    # cu sqlite baza de date este un fisier
    #
    dir_curent = os.path.abspath(os.path.curdir)
    nume_fisier_bd = os.path.join(dir_curent, "bd_demo.sqlite")
    print(f"DBG: fisier baza date sqlite:", nume_fisier_bd)

    bmd = BDNumeSiSalut(nume_fisier_bd)
    bmd.creaza_conexiunea()
    bmd.initializeaza_baza_de_date()

    el_bd = bmd.selecteaza_nume_si_salut()
    print("DBG: elemente baza de date")
    for el in el_bd:
        print(f"Nume: {el[0]:10}: salut: {el[1]}")

    bmd.inchide_conexiunea()