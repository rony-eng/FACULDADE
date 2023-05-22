# implementar uma solução em Python que faça o tratamento de exceção
# de divisão por zero.
def dividir(x, y):
    try:
        resultado = x/y
        print('A resposta é:', resultado)
    except ZeroDivisionError:
        print('Divisão por zero.')