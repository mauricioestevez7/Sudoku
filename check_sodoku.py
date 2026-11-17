def es_cuadrada(matriz:list) -> bool:
    return len(matriz[0]) == len(matriz)

def es_lista(lista:list=False) -> bool:
    
    try:
        if lista == []: return True
        lista[0] = lista[0]
        lista = [0]
        return True
    except:
        return False

def check_duplicados(lista:list) -> bool:
    return len(lista) != len(set(lista))

def check_columna(matriz:list, columna:int) -> bool:
    assert isinstance(columna, int)

    lista = []
    for indice in range(len(matriz)):
        lista.append(matriz[indice][columna])
    
    return not check_duplicados(lista)

def check_fila(matriz:list, fila:int) -> bool:
    assert isinstance(fila, int)
    return not check_duplicados(matriz[fila])

def es_entero(matriz:list) -> bool:
    for lista in matriz:
        for valor in lista:
            if not isinstance(valor, int):
                return False
    return True

def check_sodoku(matriz:list) -> bool:
    if not(es_cuadrada and es_lista(matriz) and es_entero(matriz)):
        return False
    for indice_de_matriz in range(len(matriz)):
        if not (check_columna(matriz, indice_de_matriz) and check_fila(matriz, indice_de_matriz)):
            return False
    return True







if __name__ == "__main__":
    
    # TEST es_cuadrada
    assert es_cuadrada([
        [1, 2, 3],
        [1, 2, 3],
        [0, 0, 0]
    ])

    assert not es_cuadrada([
        [1, 2, 3],
        [1, 2, 3],
        [0, 0, 0],
        [0, 0, 0]
    ])

    assert es_lista([1, 2, 3])
    assert es_lista([])
    assert es_lista([0])
    assert not es_lista(1)
    assert not es_lista()
    assert not es_lista((1, 2, 3))
    assert not es_lista(False)


    assert not check_duplicados([1, 2, 3])
    assert check_duplicados([2, 3, 3])
    assert not check_duplicados([1])
    assert not check_duplicados([0, 1, 2, 3, 4])


    assert not check_columna([
        [1, 2, 3],
        [1, 2, 3],
        [2, 3, 3]
    ], 2)

    assert check_columna([
        [2, 2, 3],
        [0, 2, 3],
        [1, 3, 3]
    ], 0)

    assert not check_columna([
        [2, 2, 4],
        [0, 2, 3],
        [1, 3, 3]
    ], 2)

    assert es_entero([
        [1, 1, 1],
        [1,2,3,4],
        [11111]
    ])
    assert not es_entero([
        [1, 1, 1],
        [1,2,3,4],
        ["11111"]
    ])
    assert not es_entero([
        [1, 1, 1],
        [1,2,3,4],
        [11.5, 1, 1, 1]
    ])
    assert not es_entero([
        [1, 1, 1],
        [1,2,[3],4],
        [1, 1, 1, 1]
    ])
