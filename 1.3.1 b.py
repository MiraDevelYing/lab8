import numpy as np  
from copy import copy


def unionPairs(n):  
    for item in range(n):
        for jtem in range(n):
            yield item, jtem


while True:
    matrix_A = np.zeros([3, 3], dtype=float)  
    for i, j in unionPairs(3):
        try:
            matrix_A[i][j] = int(input(f'A[{i + 1}][{j + 1}]: '))  
        except ValueError:
            print('Тільки числа!')
            break
    else:
        print(f'Матриця А:\n{matrix_A}')  
        matrix_B = copy(matrix_A)
        for a in range(3):
            for b in range(3):
                matrix_B[a][b] = matrix_A[b][a] 
        print(f'Транспонована матриця А:\n{matrix_B}')  
        if input('CONTINUE - Enter, BREAK - something'):
            break
