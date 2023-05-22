import threading
import time

# exemplo de função sem parametros
def Funcao():
    for i in range(3):
        print(i,'Executando a Thread')
        time.sleep(1)

print('Iniciando o programa!')
threading.Thread(target=Funcao).start()
print('Finalizando o programa!')