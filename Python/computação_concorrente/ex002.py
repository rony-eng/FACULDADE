# implementar uma solução em Python, através do uso de Thread, que faça:
# a. inicie a execução de duas Threads;
# b, coloque a primeira e a segunda threads para esperar,
# respectivamente, 3 e 2 segundos
# informe a ordem da execução das threads
from time import sleep
from threading import Thread
def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')

t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join()# esperar até completar a execução da thread 1
t2.join()# esperar até completar a execução da thread 2
print('A execução foi concluída!')