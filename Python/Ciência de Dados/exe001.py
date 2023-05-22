#carregar dados da base load_digits. Informar a quantidade de dados.
from sklearn.datasets import load_digits
digitos = load_digits()

#existem 1797 imagens, sindo que cada uma tem uma dimensão 8 x 8 = 64
print("Shape dos dados de imagem:{}".format(digitos.data.shape))
#apresentar o total de dados rotulados com inteiros de 0 a 9
print("Shape dos dados rotulados:{}".format(digitos.target.shape))