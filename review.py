x=[numero_par for numero_par in range(1,101) if numero_par%2==0]
print(x)
par=lambda t: t%2==0
for numero in range(0,101):
    if par(numero):
        print(numero)
        