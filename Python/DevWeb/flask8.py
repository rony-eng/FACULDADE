from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('ola.html')
 
@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá, ", nome_recebido = nome
 
if __name__ == '__main__':# para testar a funcionalidade do arquivo atual, python assumi automaticamente __main__ quando é executado
    app.run()