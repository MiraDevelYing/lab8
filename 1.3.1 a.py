import numpy as np  

while True:
    try:
        matrix = np.array(list(map(float, input('Введіть лінійний масив: ').split())),
                          dtype=float)  
    except ValueError:  
        print('Тільки числа!\n')
        continue
    else:
        print(f'Обернений масив: {list(reversed(matrix))}')  

    if input('\nCONTINUE - Enter, BREAK - something'):
        break
