from flask import Flask, render_template, request, url_for, current_app, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cheie pentru formular'

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

    str_url = b_url + url_for('exemplu_bd')
    ret += '<a href=' + str_url + '>' + str_url + '</a>\n'

    ret += '</pre>'

    ret += '</h3>'

    ret += "<h3>Documentatie:</h3>"
    ret += " - HTML/CSS etc.: <a href = https://www.w3schools.com/html/default.asp>w3schools</a></br>"
    ret += " - FLASK:        <a href = https://flask.palletsprojects.com>site framework flask</a>"

    return ret

@app.route("/salut/")
@app.route("/salut/<nume>")
def salut(nume = None):
    if nume == None:
        return "Salut"
    else:
        return f"Salut {nume}"
    
@app.route("/exsablon1")
def exsablon1():
    return render_template("sablon1.html")


@app.route("/salut_formular1", methods = ['GET', 'POST'])
def salut_formular1():
    
    '''
    print("Nume formular:", request.get_data())
    print("Numele din formular:", request.form.get("nume"))
    print("Submit:             ", request.form.get("submitnume"))
    '''

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

@app.route("/exbd", methods = ['GET', 'POST'])
def exemplu_bd():
    form_dict = request.form.to_dict()
    return render_template('democomplet.html', pagina=url_for('exemplu_bd'))
