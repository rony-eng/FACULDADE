#Implementar uma solução em Python com Flask que faça:

#1. Exiba a mensagem: “Página principal” no endereço raiz de uma página web
#2. Exiba a mensagem: “Olá, mundo!” no enddereço “/ola/” de uma página web
#3. Exiba a mensagem: “Olá, usuário!” no endereço “/ola/nome_do_usuário “ de uma página web
from flask import Flask

app = Flask(__name__)

@app.route('/')# a rota, vai fazer referência a def index
def index():
    return "Página Principal"

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá, ' + nome + '!'

if __name__=='__main__':# para testar a funcionalidade do 
    app.run()           # arquivo atual, python assumi
                        # automaticamente __main__ quando é executado