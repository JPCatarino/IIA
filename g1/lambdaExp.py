# Expressoes-lambda e funçoes de ordem superior
# JPCatarino 2019 

import math

# 1. (Implementar na forma de uma expressao-lambda:) Dado um número inteiro, retorna True
# caso o número seja impar, e False caso contrário.
isOdd = lambda num : num % 2 != 0

# 2. (Implementar na forma de uma expressao-lambda:) Dado um número, retorna True caso
# o número seja positivo, e False caso contrário.
isPositive = lambda num : num > 0

# 3. (Implementar na forma de uma expressao-lambda:) Dados dois números, x e y, retorna
# True caso |x| < |y|, e False caso contrário.
compareAbsolute = lambda x,y : abs(x) < abs(y)

# 4. (Implementar na forma de uma expressao-lambda:) Dado um par (x,y), representando
# coordenadas cartesianas de um ponto no plano XY, retorna um par (r,θ), correspondente
# às coordenadas polares do mesmo ponto.
polarCoord = lambda x,y : (math.sqrt(x**2 + y**2), math.atan2(y,x))

# 5. Dadas tres funcoes de duas entradas, f, g e h, retorna uma funcao de tres entradas, x, y e
# z, cujo resultado e dado por: h(f(x,y),g(y,z).
def iDKHTCT(f,g,h):
    return lambda x,y,z : h(f(x,y), g(y,z))

# 6. Dada uma lista e uma funcao booleana unária, retorna True caso a funcao tambem retorne
# True para todos os elementos da lista, e False caso contrário. ( Quantificador universal )
def uniQuant(f, gList):
    
    if not gList:
        return True
    
    if f(gList[0]):
        return uniQuant(f, gList[1:])
    else:
        return False

# 7. Dada uma lista e uma funcao booleana unária, retorna True caso a funcao retorne True para
# pelo menos um dos elementos da lista, e False caso contrário. ( Quantificador existencial )
def exQuant(f, gList):

    if not gList:
        return False
    
    if f(gList[0]):
        return True
    else:
        return exQuant(f, gList[1:])

# 8. Dadas duas listas, retorna True se todos os elementos da primeira lista tambem ocorrem
# na segunda, e False caso contrário. ( subconjunto )
isSubset = lambda l1,l2 : any(x in l1 for x in l2)
    

## TODO: REDO MAIN() TO INCLUDE PROPER TESTS INSTEAD OF PRINTS
def main():
    print(isOdd(5))
    print(isOdd(4))

    print(isPositive(1))
    print(isPositive(-2))

    print(compareAbsolute(3,4))
    print(compareAbsolute(-10,1))

    print(polarCoord(3,4))

    f = lambda x, y: x + y
    g = lambda x, y: x - y
    h = lambda x, y: x * y

    t = iDKHTCT(f, g , h)

    print(t(1,0,1))

    list1 = [1,1,1,1]
    list2 = [2,1,2,1]
    list3 = [2,2,2,2]

    print(uniQuant(isOdd, list1))
    print(uniQuant(isOdd, list2))

    print(exQuant(isOdd, list2))
    print(exQuant(isOdd, list3))

if __name__ == "__main__":
    main()