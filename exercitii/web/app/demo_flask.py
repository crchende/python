from flask import Flask, render_template, request, url_for, current_app, session, redirect

# biblioteci pentru formulare.
# vin in pachetul flask-wtf (flask what the form)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
    FileField, RadioField, BooleanField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cheie pentru formular'

class ExFormWTF(FlaskForm):
    nume = StringField("Numele: ", validators=[DataRequired()])
    submit = SubmitField("SubmitFormularWtf")

#################################################
# RUTE WEB
#################################################

# -----------------------------------------------
# Pagina principala
# -----------------------------------------------
@app.route("/")
def index():
    b_url = request.base_url.rstrip('/')
    ret = "<h1>Exemplu simplu de apliicatie web cu python si flask</h1>"
    ret += "<i><font color='gray'>cip_chende@yahoo.com</font></i>"
    ret += "<h2>URL-uri suportate:</h2>"
    ret += '<h3>'
    ret += '<pre>'
    # url_for(<nume_functie_view>)
    str_url = b_url + url_for('salut')
    ret += '<a href=' + str_url + '>' + str_url + '</a>\n'

    ret += b_url + url_for('salut', nume='nume') + '\n'
    ret += b_url + url_for('exsablon1') + '\n'
    ret += b_url + url_for('salut_formular1') + '\n'
    ret += b_url + url_for('salut_2formulare') + '\n'

    str_url = b_url + url_for('exemplu_bd')
    ret += '<a href=' + str_url + '>' + str_url + '</a>\n'

    ret += '</pre>'

    ret += '</h3>'

    ret += "<h3>Documentatie:</h3>"
    ret += " - HTML/CSS etc.: <a href = https://www.w3schools.com/html/default.asp>w3schools</a></br>"
    ret += " - FLASK:        <a href = https://flask.palletsprojects.com>site framework flask</a>"

    return ret


# -----------------------------------------------
# Date trimise in URL, prin GET
#
# Variabila trimisa direct prin URL: <nume>
#   variabila 'nume' a functiei va prelua 
#       elementul <nume> din URL
#
# URL cu parametrii: 
#   http://127.0.0.1:5010/salut/ciprian?x=1&y=2
#
# Prin GET se pot transmite diversi parametrii.
# In exemplul de mai sus avem: 
#   x = 1
#   y = 2
# care pot fi regasiti in request.args si pot fi
# obtinuti cu: request.args.get('x') -> 1
# -----------------------------------------------
@app.route("/salut/")
@app.route("/salut/<nume>")
def salut(nume = None):
    if nume == None:
        ret_str = "Salut"
    else:
        ret_str = f"Salut {nume}"

    # Obiectul request contine forarte multe informatii
    # print(dir(request)) # pentru a vedea compooentele obiectului

    print("DBG: request.host:       ", request.host)
    print("DBG: request.url:        ", request.url)
    print("DBG: request.user_agent: ", request.user_agent)

    # items - generator
    print("DBG: request.args:", list(request.args.items()))
    
    # obtinerea parametrilor din linia de comanda:
    print("DBG: request.args.get('x'):", request.args.get('x'))

    return ret_str

# -----------------------------------------------
# Utilizare sablon
# 
# In exemplele anterioare raspunsul era construit in
# functia view.
#
# Aici, functia view foloseste un sablon html, fisierul
#   sablon1.html 
#       din directorul 
#   templates
# -----------------------------------------------
@app.route("/exsablon1")
def exsablon1():
    return render_template("sablon1.html")



# -----------------------------------------------------------
# Preluare si procesare date din formularul din pagina web.
#
# Obiecte:
#   request: contine ce se trimite din browser spre server
#        request.method: metoda prin care au fost trimise datele
#
#   request.form: obiectul formular
#
# Preluare date sub forma de dictionar, cu metoda to_dict():
#
#   date_formular = request.form.to_dict()
# -----------------------------------------------------------
@app.route("/salut_formular1", methods = ['GET', 'POST'])
def salut_formular1():
    
    form_dict = request.form.to_dict()
    print("Datele din formular sub forma de dictionar:", form_dict)

    salut = None

    if len(form_dict) == 0:
        # ramura pe care se intra cand se dar URL-ul
        # si la redirect - dupa ce se apasa butonul din fromular
        print("DBG: request.method = ", request.method)
        print("DBG: Nu s-a tastat nici un nume")
        #session['salut'] = salut # cazul in care accesez pagina prin URL, nu dau click pe buton
    else:
        print("DBG: request.method = ", request.method)
        print("DBG: S-au trimis datele din formular")
        nume = form_dict['nume'] # numele dat in formular
        if nume != '':
            salut = "Salutare " + nume + '!'
        else:
            salut = 'Tastati va rog un nume si apasati butonul!'

        session['salut'] = salut
        # Fara redirect, 'page reload' va retransmite datele din formular
        # 'page reload' foloseste ultima metoda folosita pentru incarcarea paginii:
        #  - POST in acest caz.
        # redirect apeleaza pagina cu GET.
        return redirect(url_for('salut_formular1'))
    
    print('salut:', salut, session.get('salut'))

    return render_template("sablon_formular1.html", salut = session.get('salut'))

# -------------------------------------------------------
# O pagina cu doua formulare - distinctie intre formulare
# -------------------------------------------------------
@app.route("/salut_2formulare", methods = ['GET', 'POST'])
def salut_2formulare():

    form_dict = request.form.to_dict()
    print("Datele din formular sub forma de dictionar:", form_dict)

    # pentru ca nu fac redirect, la reload pagina, se primeste mesajul
    # ca datele din POST vor fi trimise din nou
    return render_template("sablon_2formulare.html", date_formular = str(form_dict))


# -------------------------------------------------------
# Pagina care foloseste un formular generat cu flask wtf
# -------------------------------------------------------
#https://wtforms.readthedocs.io/en/2.3.x/fields/
class ExFormWtf(FlaskForm):
    nume = StringField("Numele: ", validators=[DataRequired()])

    check_box = BooleanField("Activare ")

    radios = RadioField("Optiuni Radio:", choices = [(1, "UNU"), (2, "DOI"), (3, "TREI")], default=3)

    lista_selectie = SelectField("Selecteaza din lista", \
                                 choices = [("el1", 1), ("el2", "doi"), (3, "el3")],\
                                            default='el2',\
                                 option_widget="height: 3")

    submit = SubmitField("SubmitFormularWtf")

@app.route("/ex_formular_wtf", methods = ['GET', 'POST'])
def fc_view_form_wtf():
    form = ExFormWtf()
    form.check_box.checked = 0
    #form.radios.default = 2
    #form.lista_selectie.default = 'doi'

    date_formular = request.form.to_dict()
    print("DBG: date_formular: ", date_formular)

    return render_template('sablon_formular_wtf.html', form = form)


# -------------------------------------------------------
# Pagina care citeste date dintr-o baza de date
# -------------------------------------------------------
@app.route("/exbd", methods = ['GET', 'POST'])
def exemplu_bd():
    form_dict = request.form.to_dict()
    return render_template('democomplet.html', pagina=url_for('exemplu_bd'))


#################################################
# COMENZI CLI
#################################################
# apel din linia de comanda:
# flask --app demo_flask testcli
@app.cli.command()
def testcli():
    print("current_app:", current_app)
    print("app.name: ", app.name)
    print(current_app.app_context())
    #print(session)