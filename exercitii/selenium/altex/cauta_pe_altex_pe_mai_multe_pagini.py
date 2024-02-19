import time
from selenium import webdriver as wd

import re; # vom parsa textul din diverse elemente din pagina

# xpath-uri pentru elemente din pagina Altex
from altex_x_paths import *

browser_folosit = "Firefox"
wb = wd.Firefox()
wb.delete_all_cookies()

url = "https://altex.ro/home"

de_cautat = "telefoane" #- merge cautarea fara probleme
#de_cautat = "masina de spalat" #- merge cautarea fara probleme

#de_cautat = "laptopuri"; # In aceleasi conditii ca si mai sus, cautarea esueaza
#                     vezu o rezolvare in cauta_altex_err_access_denied.py
###############
# Mesaj generat:
#Access Denied
#You don't have permission to access "http://altex.ro/laptopuri/cpl/" on this server.

#Reference #18.1fa13554.1622636557.58af80a4 
##############

print("\n1) INFO: Pornire Browser: {}. Cautare URL: {}".format(browser_folosit, url))
web_pg = wb.get(url)


# gasire entry-box "Search"
print("\n2) INFO: Cautare etry-box Cautare / Search in pagina principala")
print("DBG: xpath = ", entry_cauta)
e_search = wb.find_element_by_xpath(entry_cauta)

# atribute / proprietati enry-box
# exista o suprapunere intre atribute si proprietati; de multe ori se poate folosi fie get attribute fie get_property
# o diferenta ar fi ca proprietatile sunt cele configurabile de client - ex. checkbox 'ischecked'
e_search_attr = {}
e_search_attr["cl"] = e_search.get_attribute("class")
e_search_attr["inputmode_attr"] = e_search.get_attribute("inputmode") #doar attribyte, nu este si property
e_search_attr["inputmode_property"] = e_search.get_property("inputmode")
e_search_attr["placeholder_attr"] = e_search.get_attribute("placeholder")
e_search_attr["placeholder_property"] = e_search.get_property("placeholder")


print("INFO: Gasit 'Entry Search': \n \
    class: {};\n \
    attribute 'inputmode' : {}; \n \
    property  'inputmode' : {}; \n \
    attribute 'placeholder: {}; \n \
    property  'placeholder: {}."\
    .format(
        e_search_attr["cl"], 
        e_search_attr["inputmode_attr"],
        e_search_attr["inputmode_property"],
        e_search_attr["placeholder_attr"],
        e_search_attr["placeholder_property"]))


print("\n3) INFO: Utilizare functie cautare pentru a cauta telefoane:")
e_search.clear() # ne asiguram ca nu este nimic tastat in e_search
time.sleep(0.2)
e_search.send_keys(de_cautat)
print("DBG: e_search.get_attribute/property('value') = ", e_search.get_attribute("value"))
e_search.submit()
print("DBG: astept 5 secunde sa se incarce pagina. !!! Varianta 'brute force', ajuta dar uneori pagina se incarca mai tarziu ...")
time.sleep(5)

print("\n4) INFO: Rezultat cautate:")
produse = wb.find_elements_by_class_name("Products-item")

def gasire_denumire_si_pret(produs):
    #Link produs <a href ...>
    p_a = produs.find_element_by_xpath(link_asociat_poza_produs) #obiect - corespunzator element HTML <a ...>
    denumire = p_a.get_attribute("title")
    
    p_pret_int = produs.find_element_by_class_name("Price-int") #obiect - corespunzator element HTML <span class=Price-int>pret</span>
    p_pret_dec = produs.find_element_by_class_name("Price-dec")
    pret_int = p_pret_int.text # text-ul din elementul HTML
    pret_dec = p_pret_dec.text[-2:]
    pret = pret_int + "." + pret_dec
    
    return(denumire, pret)

def afiseaza_n_produse(lst_obj_prod, n_de_afisat):
    for t_p in enumerate(lst_obj_prod):
        #t_p - tuplu produs; 2 elemente: id - t_p[0] si valoare - t_p[1]
        print("DBG: ", t_p[0], t_p[1])
        denumire, pret = gasire_denumire_si_pret(t_p[1])
        print("DBG:    denumire produs: ", denumire)
        print("DBG:    pret produs:     ", pret)
        print("\n")
        
        if t_p[0] == n_de_afisat:
            print("DBG: ... Lista poate continua pana la: ", len(produse), "mesajul de debug se opreste aici.")
            break


print("DBG: rezultatul cautarii este o lista de obiecte, corespunzatoare la elemente container din interfata WEB")
afiseaza_n_produse(produse, 10)


print("\n5) INFO Trecere la pagina urmatoare")
top_div_next_pg = wb.find_element_by_xpath("//main/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
text_label = top_div_next_pg.find_element_by_xpath("label")
print("DBG: Gasit div paginatie; eticheta: {}".format(text_label))

sel = top_div_next_pg.find_element_by_xpath("div/select")
selected_option = top_div_next_pg.find_element_by_xpath("div/select/option[@selected]")
print("DBG: Selected option text: ", selected_option.text)
re_pg_sel = re.match("([0-9]+) / ([0-9])+", selected_option.text)
print("DBG: Rezultate parsare: ")
print("DBG:    re_pg_sel.groups: ", re_pg_sel.groups, "")
print("DBG:    re_pg_sel.regs:   ", re_pg_sel.regs,   " - tuplu de tupluri cu indecsii unde avem match - tot + unde avem subpattern, marcat cu () in expresia regulata")
print("DBG:    re_pg_sel.re:     ", re_pg_sel.re,     " - pattern-ul de text pe care-l cautam")
print("DBG:    re_pg_sel.group(0)", re_pg_sel.group(0), " - Ce a prins expresia regulata - tot")
print("DBG:    re_pg_sel.group(1)", re_pg_sel.group(1), " - Ce a prins expresia regulata - prima paranteza")

pg_selectata = re_pg_sel.group(1)
max_pg = re_pg_sel.group(2)

print("Pagina selectata este: ", pg_selectata)

link_inainte = top_div_next_pg.find_element_by_xpath("a")
print("DBG: gasit link inainte: ", link_inainte.get_attribute("title"))
link_inainte.click()

print("DBG: asteptam sa se incarce pagina ~ 4 sec")
time.sleep(4)
print("DBG: - afisam primele produse din pagina 2")
produse = wb.find_elements_by_class_name("Products-item")
afiseaza_n_produse(produse, 10)

'''
print("\n6) INFO: Cautam si afisam primele rezultate din toate paginile disponibile: {} pagini".format(max_pg))
for i in range(max_pg)
    produse = wb.find_elements_by_class_name("Products-item")
    afiseaza_n_produse(produse, 10)
'''

print("DBG: Browser-ul se va inchide in 5 secunde:")
time.sleep(5)
wb.close()

        


