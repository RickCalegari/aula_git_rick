numero = int(input('digite um número:'))

#enquant
  
def valdiador(numero):
    contador = 2
    primo = True
    while contador < numero:
        if numero % contador == 0:
            primo = False
        contador += 1

    return primo


print(valdiador(numero))
#