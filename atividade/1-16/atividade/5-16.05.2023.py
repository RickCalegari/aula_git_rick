notas = input("digites suas notas separando por virgulas: ")
def media(notas):
    calculo = len(notas.split(','))
    resultado = 0
    for nota in notas:
        if nota != ",":
            resultado = resultado + float(nota)
    return resultado / calculo

print("sua média final é: " + str(media(notas)))