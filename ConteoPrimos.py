"""
Realizar el conteo de todos los numeros primos menores que 100, usando el principio de inclusion exculsion 
y generando la lista o conjuntos de los elementos correspondientes para el calculo y luego muestre el listado
de todos los numeros primos menores que 100 usando algunas listas o conjuntos que uso el calculo anterior
"""

#Criba de eratóstenes: 
#principio de inclusión-exclusión con el fin de encontrar el numero de primos menor o igual a un numero n

n = 100

def CribaErastostenes(n):
#Array booleano, si es primo = True, si no = False    
    primo = [True for i in range(n+1)]
    #menor primo posible
    a = 2
    while (a*a < n):
        #no cambio en primo = primo y viceversa
        if (primo[a] == True):
            for i in range(a*a, n+1, a):
                primo[i] = False         
        a += 1
