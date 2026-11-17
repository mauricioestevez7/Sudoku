def es_cuadrada(matriz:bool) -> bool:
    return len(matriz[0]) == len(matriz)

def check_sodoku(matriz:bool) -> bool:
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
