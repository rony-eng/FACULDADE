from functools import reduce
f_soma = lambda x,y: x + y
# considere a lista abaixo:
numeros = [1,2,3,4,5,6,7,8,9,10]

# implementar uma solução através de programação funcional para
# somar todos os elementos da lista.
resultado = reduce(f_soma, numeros)
print(resultado)