import time
from selenium import webdriver as wd

# xpath-uri pentru elemente din pagina Altex
from altex_x_paths import *

browser_folosit = "Firefox"
wb = wd.Firefox()
wb.delete_all_cookies()

url = "https://altex.ro/home"

#de_cautat = "telefoane"         #cautare OK
#de_cautat = "masina de spalat"  #cautare OK

de_cautat = "laptopuri"          #nu functioneaza. EROARE:
###############
# Mesaj generat:
#Access Denied
#You don't have permission to access "http://altex.ro/laptopuri/cpl/" on this server.

#Reference #18.1fa13554.1622636557.58af80a4 
##############

#Daca la un moment dat avem eroare - ex. se incarca pagina "Access Denied", toate referintele la obiectele
#paginii se vor pierde.
#Adica e_search care este identificat prin wb.find_element_by_path(entry_cauta) trebuie actualizat.
#Altfel apar erori de genul:
#
#selenium.common.exceptions.StaleElementReferenceException: 
#Message: The element reference of [object String] "{\"element-6066-11e4-a52e-4f735466cecf\":\"40a3105e-88e2-4838-a426-f4becb8c5364\"}" is stale; 
#either the element is no longer attached to the DOM, it is not in the current frame context, or the document has been refreshed

# Abordare
# Variabilele in care pastram ID-ul elementelor / obiectelor din pagina, trebuie actualizate daca apar erori de incarecare a paginii
#
# La fiecare incarcare a paginii, trebuie sa vedem daca avem sau nu erori
# - Se verifica fie titlul paginii - daca este "Access Denied" sau
#   Continutul:
#   pg_err_msg = wb.find_element_by_xpath("/html/body/h1")
#   pg_err_msg.text
#    -> 'Access Denied'
#
# In caz de eroare, se citeste URL-ul care s-a dorit sa fie accesat:
#   url_cautat = wb.current_url
# Se sterg toate cookie-urile:
#   wb.delete_all_cookies()
# Se incearca din nou accesarea paginii cautate:
#   wb.get(url_cautat)


####################################################
# FUNCTII
####################################################

####################################################
# Gasire 'entry' cautare/search in pagina principala
####################################################
def gaseste_entry_search(x_path_entry_cauta):
    e_search = ""
    
    try:
        # gasire entry-box "Search"
        print("DBG: xpath = ", x_path_entry_cauta)
        e_search = wb.find_element_by_xpath(x_path_entry_cauta)

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

    except Exception as e:
        print("EROARE. Nu gasesc x_path-ul in pagina:", e)
        e_search = "ERROR"

    print("e_search = ", e_search)
    return e_search


#######################################################
# Folosire functie de cautare - asociata cu entry-ul cautare de pe site
#######################################################
def cauta_pe_site(id_obj_cautare, de_cautat, x_path_entry_cauta):
    global wb
    cauta = 1
    max_incercari = 3
    nr_incercari = 1
    
    id_obj_cautare.clear() # ne asiguram ca nu este nimic tastat in e_search
    time.sleep(0.2)
    id_obj_cautare.send_keys(de_cautat)
    print("DBG: e_search.get_attribute/property('value') = ", id_obj_cautare.get_attribute("value"))
    id_obj_cautare.submit()
    print("DBG: astept 5 secunde sa se incarce pagina. !!! Varianta 'brute force', ajuta dar uneori pagina se incarca mai tarziu ...")
    time.sleep(5)
        

    while (cauta and nr_incercari <= 3):
        
        print("Verificare ca s-a incarcat pagina dupa search (ar trebui sa am entry-ul cautare disponibil in pagina)")
        e_search = gaseste_entry_search(x_path_entry_cauta)
        
        if e_search != "ERROR":
            print("!!! BINE, Bine - am gasit e_search")
            cauta = 0
        else:
            print("Pagina nu s-a incarcat bine ... stergem cookie-urile (posibil si cache-ul) si mai incercam ...")
            url_curent = wb.current_url; # dupa ce scriem ceva in entry-ul de cautare si facem submit, se modifica URL-ul
                                         # URL-ul acesta ar trebui sa ne duca la artcolele cautate - a fost format dupa "Enter"
                                         # in entry-ul de cautare in care s-a inclus textul de cautat.
            
            print("URL-ul de accesat: ", url_curent)            
            wb.delete_all_cookies()
            web_pg = wb.get(url_curent)
            time.sleep(1)
            nr_incercari += 1
            
        if nr_incercari > 3:
            print("EROARE cautare")
            e_search = "ERROR"
        
    return e_search
            

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

#######################################################
#######################################################

print("\n1) INFO: Pornire Browser: {}. Cautare URL: {}".format(browser_folosit, url))
web_pg = wb.get(url)


print("\n2) INFO: Cautare etry-box Cautare / Search in pagina principala")
e_search = gaseste_entry_search(entry_cauta)
if e_search == "ERROR":
    url_curent = wb.current_url
    web_pg = wb.get(url)
    e_search = gaseste_entry_search(entry_cauta)

print("\n3) INFO: Utilizare functie cautare pentru a cauta telefoane:")
e_search = cauta_pe_site(e_search, de_cautat, entry_cauta)

print("\n4) INFO: Rezultat cautate:")
produse = wb.find_elements_by_class_name("Products-item")


print("DBG: rezultatul cautarii este o lista de obiecte, corespunzatoare la elemente container din interfata WEB")

for t_p in enumerate(produse):
    #t_p - tuplu produs; 2 elemente: id - t_p[0] si valoare - t_p[1]
    print("DBG: ", t_p[0], t_p[1])
    denumire, pret = gasire_denumire_si_pret(t_p[1])
    print("DBG:    denumire produs: ", denumire)
    print("DBG:    pret produs:     ", pret)
    print("\n")
    
    if t_p[0] == 5:
        print("DBG: ... Lista poate continua pana la: ", len(produse), "mesajul de debug se opreste aici.")
        break

