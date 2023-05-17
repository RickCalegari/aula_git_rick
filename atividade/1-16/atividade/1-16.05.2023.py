numero1 = float(input('digite um numero:'))
numero2 = float(input('digite outro numero:'))
operação = int(input('digite sua opção (1/2/3/4):'))
def adição(numero1 ,numero2):
    return numero1 + numero2
def subtração(numero1 ,numero2):
    return numero1 - numero2
def multiplicação(numero1 ,numero2):
    return numero1 * numero2
def divisão(numero1 ,numero2):
    return numero1 / numero2

if operação == 1:
    print(adição(numero1,numero2))
if operação == 2:
    print(subtração(numero1,numero2))
if operação == 3:
    print(multiplicação(numero1,numero2))
if operação == 4:
    print(divisão(numero1,numero2))