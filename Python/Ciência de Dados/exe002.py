ml = [0,5,10,15,20,25,30]
f = lambda x: x>30
mlf = filter(f, ml)
print(list(mlf))