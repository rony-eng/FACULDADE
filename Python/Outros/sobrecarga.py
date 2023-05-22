# exemplo de sobrecarga, um pouco antes de polimorfismo
def somar(x, y, z = 0):
    return x + y+z

print(somar(20,30))
print(somar(20,30,50))