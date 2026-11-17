def es_cuadrada(matriz:list) -> bool:
    return len(matriz[0]) == len(matriz)

def es_lista(lista:list) -> bool:
    
    try:
        if lista == []: return True
        lista[0] = lista[0]
        lista = [0]
    except:
        return False

def check_sodoku(matriz:list) -> bool:
    pass




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