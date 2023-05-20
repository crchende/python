import sqlite3

class BDSqlite:
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