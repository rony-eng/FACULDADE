# faça um programa para calcular e informar o IMC (índice de massa corpórea)
# do usuário, que deverá fornecer seu peso e sua altura. IMC = peso / altura

p = eval(input('Informe seu peso: '))
a = eval(input('Informe sua altura: '))
imc = p / (a**2)
print('IMC = {:.5}'.format(imc)) 