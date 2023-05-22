# implementar uma solução em Python para visualizar dados de vendas de produtos em gráfico de barras
# por exemplo, utilize os seguintes dados:
# x = ['A','B','C','D']
# Y = [3,8,1,10]
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()