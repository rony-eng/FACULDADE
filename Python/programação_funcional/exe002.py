# considere a lista abaixo:
lista = [0,1,1,2,3,5,8,13,21,34]

# implementar uma solução através de programação funcional
# para imprimir apenas os números pares.

fTesteParidade = lambda x: x%2==0
print(f'Teste de fTesteParidade(5) = {fTesteParidade(5)}')
pares = list(filter(fTesteParidade, lista))
print(f'Lista de numeros pares = {pares}')