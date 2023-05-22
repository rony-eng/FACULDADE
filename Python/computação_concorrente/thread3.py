import threading
import time
#sincronizando threads
ls = []

def contador1(n):
    for i in range(1, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.4)
def contador2(n):
    for i in range(6, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=contador1, args=(5,))
x.start()

x.join() # faz com que só depois de finalizar a 1° thread
         # ela vá para a próxima
y = threading.Thread(target=contador2, args=(10,))
y.start()

x.join()
y.join()
print(ls)
