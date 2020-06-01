import numpy as np


def unique_pairs(n):  
    for item in range(n):
        for jtem in range(n):
            yield item, jtem


while True:
    matrix_A = np.zeros([4, 4], dtype=float)  
    matrix_B = np.zeros([4, 4], dtype=float) 
    print('Введіть елементи матриці А:')
    for i, j in unique_pairs(4):
        try:
            input_element = float(input(f'A[{i + 1}][{j + 1}]: '))  
        except ValueError:
            print('Тільки числа!\n')
            break
        else:
            matrix_A[i][j], matrix_B[i][j] = \
                input_element, input_element 
            if input_element < 0:  
                matrix_B[i][j] = 0
    else:
        print(f'Матриця А:\n{matrix_A}\n'  
              f'Матриця B:\n{matrix_B}') 
        if input('CONTINUE - enter, EXIT - something: '):
            break
    continue
