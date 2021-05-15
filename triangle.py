

def area_calculate(a,b):
    area_triangle = ((a*b)/2)
    return(area_triangle)

def triangle_kind(user_decision,a,b):
    if user_decision == "Si":
        user_triangle = str(input('¿La punta del triangulo esta en la mitad de la base? Si/No:  '))
        if user_triangle == "Si":
            side = (((a/2)**2)*((b)**2))**0.5
            if a == side:
                print('El triangulo es Equilatero')
            else:
                print('El triangulo es Isoceles')
        else:
            user_triangle_2 = str(input('¿La punta del triangulo esta en uno de los extremos? Si/No:  '))
            if user_triangle_2 == "Si":
                if a == b:
                    print('Es un triangulo Isoceles, y rectangulo')
                else:
                    print('Es un triangulo Escaleno')
            else:
                print('Es un triangulo Escaleno')
    else:
        print("Adios")

if __name__ == "__main__":
    a = int(input('Por favor ingrese la base:  '))
    b = int(input('Por favor ingrese la altura:  '))
    print (f'El área del triangulo es {area_calculate(a,b)}')
    user_decision = str(input('¿Deseas saber que tipo de triangulo es? Si/No:  '))
    triangle_kind(user_decision, a, b)

