# Funções para processamento de listas e tuplos
# JPCatarino 2019

# Retorna um par com as listas dos primeiros e segundos elementos de uma dada lista de pares
def split(gList):

    if not gList:
        return [], []

    aux = split(gList[1:])

    return [gList[0][0]] + aux[0], [gList[0][1]] + aux[1]

# Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos de l
# diferentes de x e pelo número de ocorrencias x em l.
def remove_and_count(gList, x):
    if not gList:
        return [], []
    
    aux1, aux2 = remove_and_count(gList[1:], x)

    if(gList[0] == x):
        return aux1, 1 + aux2
    
    return [gList[0]] + aux1, 0 + aux2
    
# Dada uma lista, retorna o número de ocorrencias de cada elemento, na forma de uma lista
# de pares (elemento,contagem).
def countElem(gList):
    if not gList:
        return []
    
    x = gList[0]
    auxL, counter = remove_and_count(gList, x)

    return [(x, counter)] + countElem(auxL)


