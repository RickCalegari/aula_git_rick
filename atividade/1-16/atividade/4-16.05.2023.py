frase = str(input('digite sua frase: '))
def palavras(frase):
    resultado = len(frase.split())
    return resultado
print(palavras(frase))