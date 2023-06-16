FORMULARE
===

Formularele sunt utilizate pentru a prelua date de la utilizatori.
Datele din formular vor fi transmise cu metoda POST.
Aceste date nu sunt vizibile in URL.

Si prin URL se pot trimite date dar cu metoda GET.
Aceste date sunt vizibile in URL.


Cum comunica browserul datele trimise in formular.
---
Un formular contine mai multe elemente din categoria \<input\> care permit
introducerea de date.
Aceste elemente pot fi de mai multe tipuri:
 - entry
 - submit
 - checkbox
 - radiobox
   etc.

Acestea pot avea mai multe proprietati / atribute, printre care:
 - name
 - value

La apasarea butonului aferent elementului \<input type=submit ...\> browserul preia 
datele din formular si le transmite prin metoda 'POST' catre client.


Citirea datelor din formular in program
---
Varianta cea mai directa pentru a citi datele din formular este folosirea
metodei **to_dict()**:

    date_form_dict = request.form.to_dict()

Aceasta construieste un dictionar cu *chei* numele si *valori* valorile
elementelor *\<input\>* din formular


Transmiterea numelui formularului
---
Proprietatea 'name' a unui formular este depreciata
Pentru a transmite informatii despre formularul de la care se primesc datele
Trebuie folosite numele + valoarea butonului submit
sau un camp \<input type="hidden" name="..." value="..."\>

*Varianta preferata print elementul submit folosind numele si valoarea acestuia.*

In cazul folosirii campului hidden - este nevoie de o reincarcare
a paginii - din browser, pe langa restartarea aplicatiei pentru a 
vedea valoarea actualizata - cand se schima numele si valoarea in program.

Pagina cu mai multe formulare
---
Chiar daca pagina are mai multe formulare, datele dintr-un singur formular sunt
trimise la server - cele din formularul in care se apasa butonul submit.
Datele din celelalte formulare nu se trimit.

Definirea formularelor
---
1. In format HTML: \<form\> ... \<form\> - a se vedea exemplul 1. din sectiunea exemple.

2. Ca obiect, folosind libraria flask-wtf (what the form)



Exemple:
===

**1. Formular HTML**
---

**Componenta HTML:**

        <p>Primul formular</p>
        <form id="ID_FORMULAR_1" method="POST" action="/salut_2formulare">
            <label for=id_valoare_nume>Nume:</label></br>
            <input type="hidden" id="un id" name="NUME_FORMULAR_HIDDEN" value="FORMULAR_1">
            <input id=id_valoare_nume type=text name="nume">
            <input type=submit name="FROMULAR_1_SUBMIT" value="Nume">
        </form>

        <hr/>
        
        <p>Formularul al doilea</p>
        <form id="ID_FORMULAR_2" method="POST" action="/salut_2formulare">
            <label for=id_forma_salut>Salut:</label></br>
            <input id=id_forma_salut type=text name="salut">
            <input type=submit name="FORMULAR_2_SUBMIT" value="Formula Salut">
        </form>

**Componenta Python:**
        
        from flask import request # pentru a putea prelucra datele primite din pagina web - request-urile

        form_dict = request.form.to_dict()
        
        print("Datele din formular sub forma de dictionar:", form_dict)



**Fisierul template din care fac parte formularele de mai sus este mai jos.**
    *sablon_2formulare.html*

        <div style="float: top; width: 80%; padding: 14px; background: lightcyan; border-width: 1px">
            <h1>Exemplu colectare date cu formular</h1>
        </div>

        <div id=salut style="float: left; width:40%; height: 40%; padding: 4px; border: solid blue">
            {% if salut %} 
                <pre>{{ date_formular }}</pre>
            {% else %}
                ... aici se va afisa salutul de la persoana data in formular ...
            {% endif %}
        </div>
        <div style="float: left; width: 40%; height: 40%; padding: 4px; border:solid aqua;">

            <p>Primul formular</p>
            <form id="ID_FORMULAR_1" method="POST" action="/salut_2formulare">
                <label for=id_nume>Nume:</label></br>
                <input type="hidden" id="un id" name="NUME_FORMULAR_HIDDEN" value="FORMULAR_1">
                <input id=id_nume type=text name="nume">
                <input type=submit name="FROMULAR_1_SUBMIT" value="Nume">
            </form>

            <hr/>
            
            <p>Formularul al doilea</p>
            <form id="ID_FORMULAR_2" method="POST" action="/salut_2formulare">
                <label for=id_salut>Salut:</label></br>
                <input id=id_salut type=text name="salut">
                <input type=submit name="FORMULAR_2_SUBMIT" value="Formula Salut">
            </form>

        </div>

        <div style="float: top; width: 80%; padding: 14px; background: lightgrey; border-width: 1px">
            <h2>Rand 2</h2>
            === Sfarsit pagina ===
        </div>


**Codul Python care utilizeaza teamplate-ul / sablonul de mai sus**

        from flask import Flask, render_template, request, url_for, current_app, session, redirect

        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'cheie pentru formular'

        #
        # O pagina cu doua formulare - distinctie intre formulare
        #
        @app.route("/salut_2formulare", methods = ['GET', 'POST'])
        def salut_2formulare():
            form_dict = request.form.to_dict()
            print("Datele din formular sub forma de dictionar:", form_dict)
            
            return render_template("sablon_2formulare.html", date_formular = str(form_dict))

**Datele transmise cu POST**

        - la apasarea butonului submit din **formularul 1**, cu campul entry gol:

            {'NUME_FORMULAR_HIDDEN': 'FORMULAR_1', 'nume': '', 'FROMULAR_1_SUBMIT': 'Nume'}
            127.0.0.1 - - [16/Jun/2023 21:22:24] "POST /salut_2formulare HTTP/1.1" 200 -

        - la apasarea butonului submit din **formularul 2**, cu campul entry gol:

            {'salut': 'test', 'FORMULAR_2_SUBMIT': 'Formula Salut'}
            127.0.0.1 - - [16/Jun/2023 21:24:50] "POST /salut_2formulare HTTP/1.1" 200 -

        


**2. Utilizare librarie flask-wtf (what the form)**
