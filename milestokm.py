def miles2km(numero):
    return (numero*1.609344)
def km2miles(numero):
    return (numero*0.621371)

if __name__ == "__main__":
    option = int(input("Conversor, selecciona 1 para pasar de kms a mil o 2 para mil a kms:  "))
    numero = int(input("Ingresa la cifra a convertir:  "))
    if option == 1:
        print(f'El resultado de la conversión es: {km2miles(numero)} millas')
    else:
        print(f'El resultado de la conversión es: {miles2km(numero)} kilometros')