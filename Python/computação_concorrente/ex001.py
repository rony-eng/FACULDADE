# implementar uma solução em Python, através do uso de thread, que faça:
# a. inicie a execução de uma thread
# b. Coloque a thread para esperar 2 segundos
# c. informe o início e o final da execução da thread
from time import sleep
from threading import Thread
def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')
thread = Thread(target=tarefa, args=(2, 'thread em execução'))
thread.start()
print('\nAguardando pela execução da thread...')
thread.join()
print('A execução foi concluída!')

