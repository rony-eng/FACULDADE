# Implementar uma solução em Python que some todos os números pares de uma lista.
# Por exemplo, se a lista for [10, 2, 5, 7, 6, 3], o resultado deve ser igual a 18

# estratégia 01
lista = [10,2,5,7,6,3]
n = len(lista) # o comprimento da lista 6 elementos
soma = 0
for i in range (n):
	if(lista[i]%2==0):
		soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

# estratégia 02
lista = [10,2,5,7,6,3]

soma = 0
for num in lista:
	if(num%2==0):
		soma = soma+num
print(f'O somatório dos elementos pares da lista é: {soma}')