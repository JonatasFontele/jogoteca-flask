from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def hello_world():
    lista = ['God of War', 'Skyrim', 'Valorant']
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
# app.run(host='0.0.0.0', port=8080)
