# considere a lista abaixo:
veiculos = ['aviao', 'carro', 'navio', 'ônibus']

# implementar uma solução através de programação funcional
# para transformar todos os nomes em maiusculos.
f_maiuscula = lambda x: str.upper(x)
nomes_maiusculos = list(map(f_maiuscula, veiculos))
print(f'nomes maiusculos = {nomes_maiusculos}')