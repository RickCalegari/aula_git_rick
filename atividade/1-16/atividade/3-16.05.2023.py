temperaturaC = int(input('qual é a temperatura em Celcius:'))
def calculo(celcius):
    resultado = (celcius * 9/5) + 32  
    return resultado

print(calculo(temperaturaC))