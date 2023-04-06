def crq(numero, precisao=0.0001):
    raiz = numero/2
    while abs(numero - raiz**2) > precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz
    
numero = 25
raiz = crq(numero)
print('a raiz quadrada de', numero, 'é', raiz)
# abs usando para mostrar o valor absoluto de um número
#exemplo abaixo
print(abs(-5))