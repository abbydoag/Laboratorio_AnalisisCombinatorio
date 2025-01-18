"""
Realizar el conteo de todos los numeros primos menores que 100, usando el principio de inclusion exculsion 
y generando la lista o conjuntos de los elementos correspondientes para el calculo y luego muestre el listado
de todos los numeros primos menores que 100 usando algunas listas o conjuntos que uso el calculo anterior
"""

from itertools import combinations

#Criba de eratóstenes: 
#principio de inclusión-exclusión con el fin de encontrar el numero de primos menor o igual a un numero n

n = 100

def criba_eratostenes(n):
#Array booleano, si es primo = True, si no = False 
    primo = [True for _ in range(n + 1)]
    primo[0] = primo[1] = False  # 0 y 1 no son primos
    #menor primo posible
    a = 2
    while (a*a <= n):
        #no cambio en primo = primo y viceversa
        if (primo[a] == True):
            for i in range(a*a, n+1, a):
                primo[i] = False
        a += 1
    return [i for i in range(n + 1) if primo[i]]

def inclusion_exclusion(n):
    #listas para almacenar los multiplos de cada numero primo pequeño
    conjuntos = {}
    numeros_primos = criba_eratostenes(int(n ** 0.5) + 1)  #primos necesarios para exclusion utilizando la Criba de Eratóstenes.

    #generar conjuntos de multiplos
    for primo in numeros_primos:
        conjuntos[primo] = set(range(primo * 2, n, primo))  #multiplos mayores al propio primo

    #aplicar el principio de inclusion-exclusion usando combinaciones
    union_conjuntos = set()
    for r in range(1, len(numeros_primos) + 1):
        for combinacion in combinations(numeros_primos, r):
            interseccion = set(range(2, n))
            for primo in combinacion:
                interseccion &= conjuntos[primo]
            if r % 2 == 1:  #sumar la intersección
                union_conjuntos |= interseccion
            else:  #restar la intersección
                union_conjuntos -= interseccion

    #los nmeros que no estan en la union de multiplos son primos
    todos_numeros = set(range(2, n))
    primos = todos_numeros - union_conjuntos

    #filtrar numeros incorrectos
    primos = []
    for x in todos_numeros - union_conjuntos:
        es_primo = True
        for p in numeros_primos:
            if p != x and x % p == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(x)

    return sorted(list(primos)), conjuntos

#resolviendo el problema
primos_menores_100, conjuntos_multiples = inclusion_exclusion(n)



#imprimir los resultados
print("Conjuntos generados para el cálculo:")
for primo in conjuntos_multiples:
    multiples = sorted(conjuntos_multiples[primo])
    print("Múltiplos de", primo, ":", multiples)

print("\nLista de números primos menores que 100:")
print(primos_menores_100)


