def cilinderarea(radio, altura):
    return (2*3.1415*radio*(radio+altura))

if __name__ ==  "__main__":
    print("Calculadora de volumen ")
    altura = int(input("Introduzca la altura del cilindro:  "))
    radio = int(input("Introduzca el radio del cilindro:  "))
    print (f'El área del cilindo es: {cilinderarea(radio, altura)}')