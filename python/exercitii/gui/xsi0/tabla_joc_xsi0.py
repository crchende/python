########################################################################
# Creere tabla de joc pentru x si 0
# Functionalitatea simuleaza situatia unui joc pe hartie - 2 utilizatori
# partitioneaza aceeasi hartie / tabla de joc.
#
# Aplicatia permite completarea cu x si 0 a pozitiilor de pe tabla de joc,
# verifica la fiecare mutare daca a castigat cineva, stie sa determine cand 
# cineva castiga sau cazul de remiza, cand nu castiga nimeni.
#
#
# cip_chende@yahoo.com
########################################################################

import tkinter as tk
 
########################
# Trebuie creeata o matrice cu 3 linii si 3 coloane
# Fiecare pozitie poate lua valorile X sau 0
# ex:
#  = = =
#  = = =
#  = = =
#
# Vom crea o matrice de butoane. Initial butoanele nu au nici un text.
# La apasare vor lua valorile X sau 0, in functie cine este la mutare
# Jucatoru cu X are dreptul la prima mutare
#

# Variabile de stare globale
la_mutare = "x"; # 'x' sau '0'
tabela_stari = {
    "00": "", "01": "", "02": "",
    "10": "", "11": "", "12": "",
    "20": "", "21": "", "22": "", 
}

def verifica_joc(tbl_stari):
    c = 0
    r = 0
    #verific liniile
    print("DBG: verific liniile")
    for r in range(0,3):
        da_rand_complet = 0

        print("r: ", r, tbl_stari)
        
        prim_el_r = tbl_stari[str(r)+str(0)]

        if prim_el_r == "":
            #rind incomplet, chiar de la primul element
            continue
        
        for c in range(1,3):
            print(" verificare linie, pozitia: ", c)
            if tbl_stari[str(r)+str(c)] == prim_el_r:
                da_rand_complet += 1
                
        if da_rand_complet == 2:
            return prim_el_r, "RAND", r


    print("DBG: verific coloanele")
    c = 0
    r = 0
    #verific coloanele
    for c in range(0,3):
        da_col_completa = 0
        prim_el_c = tbl_stari[str(0)+str(c)]

        if prim_el_c == "":
            #rind incomplet, chiar de la primul element
            continue
        
        for r in range(1,3):
            if tbl_stari[str(r)+str(c)] == prim_el_c:
                da_col_completa += 1
        if da_col_completa == 2:
            return prim_el_c, "COL", c

    print("DBG: verific diagonala principala (d1)")
    #verificar diagonala principala: c = r; diag_p / d1
    c = 0
    r = 0
    prim_el_d1 = tbl_stari[str(r)+str(c)]
    da_diag_p_completa = 0

    for c in range(0,3):
        if prim_el_d1 == "":
            #diagonala principala incompleta, chiar de la primul element
            continue

        if tbl_stari[str(c)+str(c)] == prim_el_d1:
                da_diag_p_completa += 1
        if da_diag_p_completa == 3:
            return prim_el_d1, "DIAG1", c
        
    print("DBG: verific diagonala secundara (d2)")
    #verificare diagonala secundara - diag_s / d2; c = 2 - r
    c = 0
    r = 2
    prim_el_d2 = tbl_stari[str(r)+str(c)]
    print("prim el d2: ", prim_el_d2)
    da_diag_s_completa = 0

    for r in range(2,-1, -1):
        c = 2 - r
        print("r: ", r, " c: ", c)
        if prim_el_d2 == "":
            #diagonala principala incompleta, chiar de la primul element
            continue

        if tbl_stari[str(r)+str(c)] == prim_el_d2:
            print("d2 ++: ", r, c)
            da_diag_s_completa += 1
        if da_diag_s_completa == 3:
            print(" ** r: ", r)
            return prim_el_d2, "DIAG2", r

    # verifica daca s-a terminat jocul. MAX 9 mutari
    mutari = 0
    for k in tbl_stari:
        if tbl_stari[k] != "":
            mutari += 1
            print("mutari facute: ", mutari)
            if mutari == 9:
                return "=", "REMIZA", ""

    # mai sunt mutari, si n-a castigat inca nimeni
    return "", "", ""
        

def actiune_buton(button_var, label_var, txt):
    global la_mutare
    print("la mutare: ", la_mutare)
    if la_mutare == "x":
        la_mutare = "0"
        img = img_0
    else:
        img = img_x
        la_mutare = "x"
    button_var.configure(text = la_mutare, image = img, state = "disable")

#    button_var.configure(text = la_mutare, state = "disable")

    label_var.configure(text = txt)
    tabela_stari[txt] = la_mutare

    #print(txt)
    #print(tabela_stari)
    
    
    print("DBG: verific stare joc")
    caracter_castigator, tip_castig, unde_castig  = verifica_joc(tabela_stari)


    # Posibil nevoie sa se mute pe server aceasta analiza.
    print ("Situatie Joc:", caracter_castigator, tip_castig, unde_castig)
    # La fiecare apasare a unui buton verific daca am castigat
    if (caracter_castigator == "x") or (caracter_castigator =="0"):
        # Unul din jucatori a castigat:
        label_var.configure(text = "Victorie: " + str(caracter_castigator) + ", " + str(tip_castig) + " " + str(unde_castig))
        fa_la_victorie()
        #resetez aceste valori. Am vazut ca uneori raman setate. Nu stiu explicatia
        #caracter_castigator, tip_castig, unde_castig = "", "", ""
    elif caracter_castigator == "=":
        label_var.configure(text = str(tip_castig))

    # Marcare loc unde ar trebui sa comunic cu serverul
    trimite_mutare_la_server(txt, la_mutare)
        
    # Marcare loc unde ar trebui sa astept mutarea adversarului
    primeste_mutare_de_la_server()
    

def joc_nou():
    global la_mutare
    # de sters tot ce este afisat pe fiecare buton
    # de resetat mesajul din bara de stare
    row = 0
    for i in range(0, 9):
        row = i // 3; #3 butoane pe linie;    i // 3 impartire fara rest; 5 / 3 = 1; 7 / 3 = 2
        #              pe prima linie vom adauga butoane de control; butoanele jocului incep de la linia 1, nu 0
        col = i % 3;  #3 butoane pe coloana;  i %  3 restul impartirii;   5 / 3 = 2; 7 % 3 = 1
        
        eval("b_"+str(row) + str(col)+".configure(text = '', image = img_nimic, state = 'normal')")
    
    l1.configure(text = "Joc Nou")
    reset_tabela_stari()
    la_mutare = "x"

        
def fa_la_victorie():
    # de sters tot ce este afisat pe fiecare buton
    # de resetat mesajul din bara de stare
    row = 0
    for i in range(0, 9):
        row = i // 3; #3 butoane pe linie;    i // 3 impartire fara rest; 5 / 3 = 1; 7 / 3 = 2
        #              pe prima linie vom adauga butoane de control; butoanele jocului incep de la linia 1, nu 0
        col = i % 3;  #3 butoane pe coloana;  i %  3 restul impartirii;   5 / 3 = 2; 7 % 3 = 1

        eval("b_"+str(row) + str(col)+".configure(state = 'disable')")

def reset_tabela_stari():
    global tabela_stari
    for k in tabela_stari.keys():
        tabela_stari[k] = ""
    print("Reset tabela stari. Valoare: \"\" pentru toate butoanele.")

def trimite_mutare_la_server(pozitie, valoare):
    #la acest moment doar afisez ce vreau sa trimit
    print("De trimisla server:", pozitie, valoare)

def primeste_mutare_de_la_server():
    global tabela_stari
    print("Aici voi astepta mutarea adversarului, prin intermediul serverului.")
    # citeste ce trimite serverul
    # alalizeaza
    # actuaizeaza interfata grafica
    

# generare dinamica butoane
# va fi generata matricea pentru x si 0 si o line care afiseaza informatii despre butonul apasat.
main_win = tk.Tk()

menu_frm = tk.Frame(main_win)  

menu_btn_joc = tk.Button(menu_frm, text = "JocNou", command = lambda: joc_nou())
menu_btn_joc.grid(row = 0, column = 0)
menu_frm.grid(row = 0, column = 0)


x_0_frm = tk.Frame(main_win)

#creere imagini de afisat pe butoane
img_x = tk.Image(file = "../imgs/mele/48x48/x.png", imgtype = "photo")
img_0 = tk.Image(file = "../imgs/mele/48x48/0.png", imgtype = "photo")
img_nimic = tk.Image(file = "../imgs/mele/48x48/nimic.png", imgtype = "photo")


#creere butoane pentru X si 0
# generare dinamica butoane
# va fi generata matricea pentru x si 0 si o line care afiseaza informatii despre butonul apasat.
row = 0
for i in range(0, 9):
    row = i // 3; #3 butoane pe linie;    i // 3 impartire fara rest; 5 / 3 = 1; 7 / 3 = 2
    #              pe prima linie vom adauga butoane de control; butoanele jocului incep de la linia 1, nu 0
    col = i % 3;  #3 butoane pe coloana;  i %  3 restul impartirii;   5 / 3 = 2; 7 % 3 = 1

    #exec("b_"+str(i)+" = tk.Button(main_win, text = "+str(i)+", command = lambda: print("+str(i)+"))")
    b_var = "b_"+str(row) + str(col)
    #                                  text = "+str(i)+
    exec(b_var+" = tk.Button(x_0_frm, text = '  ', image = img_nimic, command = lambda: actiune_buton(" + b_var + ", l1, '"+str(row) + str(col)+"'))")
    eval("b_"+str(row) + str(col)+".grid(row = "+str(row)+", column = "+str(col)+")")
    
    #print("v_"+str(i)+" = ", eval("v_"+str(i)))

x_0_frm.grid(row = 1, column = 0)


l1 = tk.Label(main_win)
l1.grid(row = 2, column = 0)
#l1.grid(row = 4, column = 0, columnspan = 3)

#Minimum window size - dimensiunile sub care fereastra nu poate fi micsorata
#
#Actiunea update_idletasks() este necesara altfel este foarte posibil sa
#se execute codul de mai jos inainte sa se afizeze fereastra. In acest caz
#nu se poate configura corect dimensiunea minima a ferestrei, nefiind widget-uri
#afisate sau fiind doar o parte din ele afisate
#
#main_win.update_idletasks()
#
#obtinerea informatiilor despre fereastra: metode 'winfo_<info_to_get>'
#valori minime fereastra fara update_idletasks()
min_width = main_win.winfo_width()
min_height = main_win.winfo_height()
print("Fereastra initiala. width: ", min_width, " height: ", min_height)

# valori minime dimensiune fereastra dupa update_idletasks
main_win.update_idletasks()
min_width = main_win.winfo_width()
min_height = main_win.winfo_height()
print("Fereastra initiala. width: ", min_width, " height: ", min_height)

#
#configurare fereastra: metode 'wm_<info_to_set>'
main_win.wm_minsize(min_width, min_height)


if __name__ == "__main__":
    print("Running as: ", __name__)
    main_win.mainloop()
else:
    print("Using as: ", __name__)
