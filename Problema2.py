def sumaPosiciones(lst, pi, pf):
    return sumaPosiciones2(lst, pi - 1, pf - 1)

def sumaPosiciones2(lst, pi, pf):

    
    if pi > pf:
        return 0
    
    
    return lst[pi] + sumaPosiciones2(lst, pi + 1, pf)


lista = [2,4,6,3]

pi = int(input("Ingrese posicion inicial: "))
pf = int(input("Ingrese posicion final: "))

print(f"Resultado: {sumaPosiciones(lista, pi, pf)}")