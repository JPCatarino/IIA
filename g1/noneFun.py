# Funções que retornam None
# JPCatarino 2019

# Dada uma lista, retornar o elemento que está à cabe¸ ca (ou seja, na posi¸ c˜ ao 0).
def listFirstElem(gList):

    if not gList or gList[0] == None:
        return None
    
    return gList[0]

#  Dada uma lista, retornar a sua cauda (ou seja, todos os elementos à excepção do primeiro).
def listTail(gList):

    if not gList or len(gList) < 2:
        return None
    
    return gList[1:]

# Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos
# homólogos.
def findEqualElems(gList1, gList2, size = None):
    
    if not gList1:
        return []
    
    if len(gList1) != size:
        print(size)
        return None
    
    aux = findEqualElems(gList1[1:], gList2, size-1)
    
    try:
        i = gList2.index(gList1[0])
        auxElem = gList2[i]
        return aux + [(gList1[0], gList2[i])]
    except ValueError:
        return aux

def findMin(gList):
    if len(gList) == 1:
        return gList[0]

    if not gList:
        return None
    
    return min(gList[0], findMin(gList[1:]))

def findMax(gList):
    if len(gList) == 1:
        return gList[0]

    if not gList:
        return None
    
    return max(gList[0], findMin(gList[1:]))

#def minAndList(gList):
#    min = findMin(gList)

# Dada uma lista de números, calcular o máximo e o m´ınimo, retornando-os num tuplo.
def findMinMax(gList):
    if len(gList) == 1:
        return gList[0]

    if not gList:
        return None
    
    return findMin(gList), findMax(gList)

#


    

def main():
    l1 = [1, 3, 4 ,5, 7]
    l2 = [1, 2, 3, 4, 7]

    print(findEqualElems(l1, l2, len(l2)))
    print(findMin(l1))

if __name__ == "__main__":
    main()
