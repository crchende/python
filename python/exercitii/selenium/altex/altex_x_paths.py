# Data verificare: 2021/05/20
# XPATH-uri din pagina: https://altex.ro/home
#
# OBS: https://altex.ro afiseaza uneori o pagina cu promotii (blackfriday ...)
# xpath-urile de mai jos nu functioneaza in acea pagina
#

#=======================
# 1. Pagina principala
#=======================
buton_altex =  "/html/body/div[@id='__next']/div[1]/div/div/div/div[2]/div[2]/a"
entry_cauta = "/html/body/div[@id='__next']/div/div/div/div/div[2]/div[4]/form/div/div/input"
div_menu_produse =   "/html/body/div[@id='__next']/div[1]/div[2]/div[2]/ul/li/ul"

#=======================
# 2. div Produse
#=======================
# Putem gasi lista de produse printr-o cautare dupa 'class_name' nu neaparat folosing xpath
#
# 2.1. produse = wb.find_elements_by_class_name("Products-item") # lista produse din partea principala a paginii
#
#      se returneaza o lista de obiecte produs
#      fiecare obiect reprezinta containerul WEB folosit pentru a prezenta un produs, care contine
#      - fotografie
#      - link
#      - pret
#      - disponibilitate - in stoc sau nu
#      - rating
#      rezervare in magazin etc

#daca folosim functia de cautare:
titlu_produse_cautate = "//main/div[2]/div[1]/div[1]/h1"

#filtre_produse_cautate = "//main/div[2]/div[2]/ul/div/li"
# sau
ul_filtre_produse_cautate = "//main/div[2]/div[2]/ul/div/ul"
li_filtre_produse_cautate = "//li" # relativ la ul

# LINK-uri relative la produs (2.1)
# Componente produs: 
link_asociat_poza_produs = "div[1]/div[1]/a"

# pret produs - nu este nevoie sa cautam dupa xpath
# se poate cauta dupa class_name in interiorul containerului produs
#    p_pret_int = produs.find_element_by_class_name("Price-int") #obiect - corespunzator element HTML <span class=Price-int>pret</span>
#    p_pret_dec = produs.find_element_by_class_name("Price-dec")









