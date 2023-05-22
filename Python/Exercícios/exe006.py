# implementar uma solução em Python que resolva a seguinte questão:
# Se nota for maior ou igual a 7, o estudante foi aprovado
# Se a nota for menor que 7 e maior ou igual a 5, o estudante está de recuperaçãp
# Se a nota for menor que 5, o estudante está reprovado.
media = eval(input('Insira sua nota: '))
if (media>=7.0):
	r = 'Aprovado'
elif(media>=5.0):
	r = 'Recuperaçãao'
else:
	r = 'Reprovado'
print(r)