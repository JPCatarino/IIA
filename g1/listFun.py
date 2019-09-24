# Funções para processamento de listas 
# JPCatarino 2019

# Retorna o comprimento de uma dada lista.
def listLen(gList):
    if not gList:
        return 0

    return 1 + listLen(gList[1:])

# Retorna soma dos elementos de uma lista de números.
def sumOfElems(gList):
    if not gList:
        return 0

    return gList[0] + sumOfElems(gList[1:])

# Verifica se um dado elemento está incluido numa dada lista. Retorna bool.
def contains(gList, gElem):
    if not gList:
        return False

    return gList[0] == gElem or contains(gList[1:], gElem)

# Retorna a concatenação de duas listas.
def concat(gList1, gList2):
    return gList1 + gList2

# Inverte uma dada lista.
def reverse(gList):
    if not gList:
        return []

    rev = reverse(gList[1:])
    rev[len(rev):] = [gList[0]]
    return rev 

# Verifica se uma dada lista é capicua. Retorna bool.
def capicua(gList):
    if len(gList) < 2:
        return True
    if gList[0] != gList[-1]:
        return False
    return capicua(gList[1:-1])

# Retorna a concatenação de uma lista de listas.
def concatLOL(LOL):
    if not LOL:
        return False

    return LOL[0] + concatLOL(LOL[1:])

# Muda todos os elementos x de uma lista para o elemento y

def substitute(gList, x, y):
    if not gList:
        return []
    if gList[0] == x:
        gList[0] = y
    return [gList[0]] + substitute(gList[1:])

#  Une duas listas e ordena
def uniteAndOrder(gList1, gList2):
    return sorted(concat(gList1, gList2))

# Cria uma lista de listas de todos os subconjuntos de um dado conjunto
def subsets(gList):
    if not gList:
        return []
    
    ss = subsets(gList[1:])
    return [[gList[0]]] + [[gList[0]] + s for s in ss] + ss

def main():
    print(subsets([1,2,3]))


if __name__ == "__main__":
    main()