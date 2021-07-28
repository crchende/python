'''
    cip_chende@yahoo.com
    
    - creere mai multe butoane, etichta in diverse cadre (frame-uri);
    - configurare proprietati fereastra principala, cadre, butoane;
    - creere obiect de tip imagine;
    - asociere imagine cu buton
    - afisare fereastra si determinare dimensiuni minime
    - configurare mod redimensionare fereastra si widget-uri
    - blocare redimensionare daca dimensiunea este sub dimensiunea minima
    
'''
from tkinter import *

#################################
# 1) Creere fereastra principala
#################################
main_win = Tk()

#################################
# 2) Folosire functii window manager - wm_<...> 
#################################
#pentru a configura titlu si alte proprietati
# ale ferestrei principale
main_win.wm_title("Cadre si butoane")

################################
# 3) Configurare proprietati widget - in acest caz, fereastra principala.
################################
# fie folosind widget["nume_proprietate"] = valoare
# fie folosind functia configure(nume_proprietate = valoare)
# Pentru orice widget, putem folosi aceste metode de a-i configura proprietatile.
main_win["background"] = "blue"
main_win.configure(relief = "groove")
main_win["borderwidth"] = 7

###############################
# 4) Creere widget-uri in fereastra principala
###############################
b_top = Button(main_win, text = "Exit", command = lambda: exit(), borderwidth=2)
frame_1 = Frame(main_win, relief = "sunken", background = "red", borderwidth=4) 
l1 = Label(main_win, text="label l1", relief = "sunken")

def cmd_btn(txt):
    print(txt)
    l1["text"] = txt

###############################
# 5) Creere widget-uri in cadrul: frame_1
###############################
f1_b1 = Button(frame_1, text = "Salut", command = lambda: l1.configure(text = "Salut"))
f1_b1.configure(background = "yellow")
f1_b2 = Button(frame_1, text = "Buna", command = lambda: cmd_btn("Buna"))
f1_b3 = Button(frame_1, text = "BINE", command = lambda: cmd_btn("__BINE__"))

################################
# 6) Afisare in interiorul frame-ului frame_1 (pana nu afisam frame_1 elementele nu vor fi vizibile)
################################
f1_b1.grid(row = 0, column = 0, sticky = (N,S,E,W), ipadx=80, ipady=15, padx=1, pady=15)
f1_b2.grid(row = 0, column = 1)
f1_b3.grid(row = 1, column = 0)

################################
# 7) Configurare coloana 0 din frame_1 ca redimensionabila
################################
frame_1.columnconfigure(0, weight = 1)


#################################
# 8) Creere frame care va contine un buton pe care afisam o imagine
#################################

#Creere frame_2 intr-o singura linie sau putem crea frame_2 iar apoi putem sa-i
#configuram proprientatile ca mai jos.
#Puteti decomenta linia de mai jos iar apoi sa le comentati pe cele 3 care fac
#actiunile separat. Se va obtine acelasi rezultat
#frame_2 = Frame(main_win, background = "cyan", borderwidth = 5)

frame_2 = Frame(main_win)
frame_2.configure(background = "cyan")
frame_2["borderwidth"] = 5

#creere obiect imagine, folosind imaginea face-smile.png din directorul ./imgs/48x48
#https://freepngimg.com/save-icon/1000043-slightly-smiling-face-emoji-free-icon-hq/48x48
#Puteti downloada imaginea de la link-ul de mai sus. In acelasi director cu 
#acest fisier, creati directorul 'imgs/48x48' si adaugati aici fisierul redenumit
#face_smile.png
#
#Gasiti mai multe imagini pe care le puteti folosi aici: https://freepngimg.com/
#
#Exercitiu - creati si alte butoane pe care incarcati alte imagini dupa modelul
#de mai jos
#
img1 = Image(file = "./imgs/48x48/face-smile.png", imgtype = "photo")
f2_b1 = Button(frame_2, image = img1, command = lambda: cmd_btn("./imgs/48x48/face-smile.png"))

f2_b1.grid(row = 0, column = 0)


################################
# 9) Afisare componente ale ferestrei principale
################################
b_top.grid(row = 0, column = 0, sticky = (N,S,E,W), pady=5)
frame_1.grid(row = 1, column = 0, sticky = (N,S,E,W), padx=10, pady=10)
l1.grid(row = 2, column = 0)

frame_2.grid(row = 3, column = 0, sticky = (N,S,E,W), pady=7)

################################
# 10) Configurare frame_2 coloana 0 si rand 0 ca redimensioabile
################################
frame_2.columnconfigure(0, weight=1)
frame_2.rowconfigure(0, weight=1)

################################
# 11) Configurare randuri si coloane redimensionabile in fereastra principala
################################
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_win.rowconfigure(3, weight=1)

################################
# 12) Fortare afisare interfata prin apelul update_idletasks()
#     Un apel main 'puternic' este update()
#     In acest caz, update_idletasks este suficient
################################
main_win.update_idletasks()

################################
# 13) Gasim dimensiunile minime ale ferestrei (fara update_idletasks ar fi 0)
################################
min_width = main_win.winfo_width()
min_height = main_win.winfo_height()
print("Fereastra initiala. width: ", min_width, " height: ", min_height)

################################
# 14) Apelam functia window manager care seteaza dimensiunile minime ale ferestrei
################################
main_win.wm_minsize(min_width, min_height)



#obligatoriu de apelat pentru a incepe bucla de evenimente
if __name__ == "__main__": 
    main_win.mainloop()
else:
    print("Using as module: ", __name__)
