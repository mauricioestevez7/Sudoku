def es_cuadrada(matriz:list) -> bool:
    return len(matriz[0]) == len(matriz)

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
