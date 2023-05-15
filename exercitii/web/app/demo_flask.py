from flask import Flask, render_template, request, url_for, current_app

app = Flask(__name__)

@app.route("/")
def index():
    b_url = request.base_url.rstrip('/')
    ret = "<h1>Exemplu simplu de apliicatie web cu python si flask</h1>"
    ret += "<h2>URL-uri suportate:</h2>"
    ret += '<h3>'
    ret += '<pre>'
    ret += '<a href=' + b_url + url_for('salut') + '>' + \
        b_url + url_for('salut') + \
        '</a>' + \
        '\n'
    ret += b_url + url_for('salut', nume='nume') + '\n'
    ret += b_url + url_for('exsablon1') + '\n'
    ret += b_url + url_for('salut_formular1') + '\n'
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
        print("DBG: Nu s-a tastat nici un nume")
    else:
        print("DBG: S-au trimis datele din formular")
        nume = form_dict['nume']
        if nume != '':
            salut = "Salutare " + nume + '!'
        else:
            salut = ''

    print('salut:', salut)

    if salut == '':
        salut = 'Tastati va rog un nume si apasati butonul!'

    return render_template("sablon_formular1.html", salut = salut)