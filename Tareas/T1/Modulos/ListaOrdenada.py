def ordenarLista(lista):
    for i in range(0, len(lista) - 1):
        for j in range(len(lista) - 1, i, -1):
            if lista[j] < lista[j - 1]:
                lista[j - 1], lista[j] = lista[j], lista[j - 1]
    return lista
