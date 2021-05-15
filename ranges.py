def boundaries(inf_limit, sup_limit, comp_limit):
    if sup_limit>comp_limit>inf_limit:
        return(print(f'El número {comp_limit} esta entre los límites dados'))
    else:
        print(f'El número {comp_limit} no esta entre los límites dados')
        new_num = int(input('Escribe un nuevo número:  '))
        return(boundaries(inf_limit,sup_limit, new_num))



if __name__ == "__main__":
    print('Este programa muestra si un número se encuentra entre dos límite, si no lo esta pide un numero nuevo.')
    inf_limit = int(input("Ingresa el límite inferior: "))
    sup_limit = int(input("Ingresa el límite superior: "))
    comp_limit = int(input("Ingresa el número de comparación: "))
    boundaries(inf_limit,sup_limit,comp_limit)