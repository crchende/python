import sqlite3
import os


class BDNumeSiSalut:
    # implicit, baza de date va fi creata in memorie
    def __init__(self, nume_baza_date="bazadatesqlite.db"):
        self.nume_bd = nume_baza_date

        self.date_initiale = (
            ("nume_si_salut", ("George", "Salut!")),
            ("nume_si_salut", ("John", "Hello!")),
            ("nume_si_salut", ("Giovani", "Ciao!")),
            ("nume_si_salut", ("Ion", "Buna ziua!"))
        )

    def creaza_conexiunea(self):
        self.conexiune = sqlite3.connect(self.nume_bd)
        self.cursor = self.conexiune.cursor()

    def creaza_tabel(self, nume_tabel, *coloane):
        #sql query
        #creare tabel
        sql_q = f"CREATE TABLE {nume_tabel}{coloane}"
        try:
            self.cursor.execute(sql_q)
        except sqlite3.OperationalError as e:
            print(f"DBG: tabelul {nume_tabel} deja exista!")
        except Exception as e:
            print(f"EROARE: Nu s-a putut crea tabelul: {e.__class__.__name__}: {e}")
            raise(e)

        #verificare:
        res = self.cursor.execute("SELECT name FROM sqlite_master")
        tbl = res.fetchone()[0]
        if tbl == nume_tabel:
            print(f"INFO: tabelul: {nume_tabel} a fost creat.")
            return 1
        else:
            print(f"EROARE: tabelul {nume_tabel} n-a putut fi creat!")
            return 0

    def insereaza_in_tabel(self, nume_tabel, *valori):
        '''
            Insereaza valori intr-un tabel.
            Parametrii:
                nume_tabel: numele tabelului in care se vor insera date
                *valori:    valorile corespunzatoare unei inregistrari (un singur rand)
                            care vor fi adaugate

            Return:
                None
        '''
        print(f"DBG: {nume_tabel}, {valori}")
        sql_q = f"INSERT INTO {nume_tabel} VALUES {valori}"
        self.cursor.execute(sql_q)
        self.conexiune.commit()

    def selecteaza_date(self, interogare_sql):
        '''
            Executa interogarea sql: interogare_sql si intoarce toate inregistrarile gasite
            sub forma unei liste de tupluri.

            Parametrii:
                interogare_sql: sirul de caractere corespunzator interogarii SQL
            
            Return:
                o lista de tupluri, corespunzatoare tuturor inregistrarilor / randurilor 
                gasite
        '''
        res = self.cursor.execute(interogare_sql)
        # o lista de tupluri: [(elemente rand 1), (elemente rand 2) ...]
        return res.fetchall()

    def inchide_conexiunea(self):
        self.conexiune.close()
    

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

    def selecteaza_nume_si_salut(self):
        sql_q = "SELECT * FROM nume_si_salut"
        return self.selecteaza_date(sql_q)

print("__name__:", __name__)
if __name__ == "__main__":
    #
    # cu sqlite baza de date este un fisier
    #
    dir_curent = os.path.abspath(os.path.curdir)
    nume_fisier_bd = os.path.join(dir_curent, "bazadatesqlite.db")
    print(f"DBG: fisier baza date sqlite:", nume_fisier_bd)

    bmd = BDNumeSiSalut(nume_fisier_bd)
    bmd.creaza_conexiunea()
    bmd.initializeaza_baza_de_date()

    el_bd = bmd.selecteaza_nume_si_salut()
    print("DBG: elemente baza de date")
    for el in el_bd:
        print(f"Nume: {el[0]:10}: salut: {el[1]}")

    bmd.inchide_conexiunea()



