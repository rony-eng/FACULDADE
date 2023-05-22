# Implementar uma solução em Python que resolva a seguinte questão:
# Calcular o valor de uma compra, sendo que o preço unitário é 10
# Se for feita uma compra de até 10 unidade, não há descontos.
# Para compras entre 11 e 20 unidades é dado um desconto de 10%
# Acima de 20 unidades, é dado um desonto de 20%
quant = eval(input('Digite a quantidade que vai comprar: '))
p_u = 10
d10 = 0.1
d20 = 0.2

if(quant <=10): # maior ou igual a 10
	v_f = p_u * quant
elif(quant <= 20): # maior que 10 e menor ou igual a 20
	v_f = p_u * quant * (1 - d10)
else: # maior que 20
	v_f = p_u * quant * (1 - d20)

print(f'O valor final da compra é: {v_f}')