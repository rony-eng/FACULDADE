import threading
import time

# exemplo de função com parametros
def Funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)

print('Iniciando o programa!')
x = threading.Thread(target=Funcao, args=('Executando',))
x.start()
print('Finalizando o programa!')