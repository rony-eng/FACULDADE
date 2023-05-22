#Implementar uma solução em Python com Flask que faça:

#1. Exiba a mensagem: ‘Olá, programador!’ no endereço raiz de uma página web e a apareça o link ‘/user/Usuário’
#2. Exiba a mensagem: ‘Olá, Usuário!’ no endereço ‘/user/’ e exiba a mensagem ‘Altere o endereços do browser e recarregue a página’
#3. Exiba a mensagem: ‘Olá, nome_usuário’ no endereço ‘/user/nome_do_usuário’ de uma página web.
from flask import Flask
app = Flask(__name__)

app.route('/')
def cumprimento():
    boas_vindas='<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/Usuário">Clique aqui!</a></p>'
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuário'):
    personalizar = f'<h1>Olá, {nome}!</h1>'
    instrucao = '<p>Altere o nome no <em> endereço do browser</em> \ e recarregue a pagina.</p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run()