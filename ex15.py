#palindromo - palacra ou frase que se pode ler 
#indiferentemente, da esquerda para a 
#direita ou vice-versa
def vp(texto):
    texto = texto.lower().replace(' ','')
    return texto == texto[::-1]
    
#texto[::-1] inverte o texto

texto = 'Socorram me subi no onibus em Marrocos'
if vp(texto):
    print(texto, 'é um palíndromo.')
else:
    print(texto, 'não é um palíndromo')#