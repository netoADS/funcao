def cf(numero):
    if numero == 0:
        return 1
    else:
        return numero * cf(numero-1)

numero = 5
fatorial = cf(numero)
print('o fatorial de', numero, 'é', fatorial)