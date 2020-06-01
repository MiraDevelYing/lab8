import random
import timeit


def linearSearch(data, number):  # Алгоритм лінійного пошуку
    n = len(data)
    counter, index = 0, 0
    while index < n and data[index] != number:
        counter += 1
        index += 1
    if index == n:
        return None, counter
    else:
        return index, counter


def binarySearch(data, number):  # Алгоритм бінарного пошуку
    midpoint = 0
    data1 = sorted(data)
    L, R = 0, len(data1) - 1
    conter1 = 0
    while L <= R:
        midpoint = (L + R) // 2
        conter1 += 1
        if data1[midpoint] == number:
            return midpoint, conter1
        elif number < data1[midpoint]:
            R = midpoint - 1
        else:
            L = midpoint + 1
    else:
        return None, conter1


def directSearch(text, pattern):  # Алгоритм прямого пошуку
    i = -1
    j, counter2 = 0, 0
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        counter2 += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
    if j == len(pattern):
        return i, counter2
    else:
        return None, counter2
    pass


_LINEAR_massive, _BINARY_massive, _DIRECT_string = [], [], ""  
# пошуки
searchLinear, searchBinary, searchDirect = int(), int(), str()  

# |||||||||||||||||||||||  LINEAR SEARCH  |||||||||||||||||||||||

print('\n<<<<<<<<<<  ЛІНІЙНИЙ ПОШУК  >>>>>>>>>>\n')
rand_or_inp_LINEAR = int(input('Введіть:\n'
                               '1 - якщо хочете ввести дані самостійно\n'
                               '2 - якщо хочете заповнити дані радномно\n>>> '))
if rand_or_inp_LINEAR == 1:  
    _LINEAR_massive = list(map(int, input('\nВведіть цілі числа через пробіл:\n>>> ').split()))
elif rand_or_inp_LINEAR == 2: 
    _LINEAR_massive = [random.randint(-10, 10) for i in range(int(input('\nВведіть кількість чисел:\n>>> ')))]

search_LINEAR_inp = int(input('\nВведіть:\n'
                              '1 - якщо хочете самостійно ввести число, яке потрібно знайти\n'
                              '2 - якщо хочете згенерувати будь-яке число в діапазоні [-10; 10]\n>>> '))
if search_LINEAR_inp == 1:  
    searchLinear = int(input('\nВведіть число:\n>>> '))
elif search_LINEAR_inp == 2:  
    searchLinear = random.randint(-10, 10)

#   BINARY SEARCH 

print('\n<<<<<<<<<<  БІНАРНИЙ ПОШУК  >>>>>>>>>>\n')
rand_or_inp_BINARY = int(input('\nВведіть:\n'
                               '1 - якщо хочете ввести дані самостійно\n'
                               '2 - якщо хочете заповнити дані радномно\n>>> '))
if rand_or_inp_BINARY == 1: 
    _BINARY_massive = sorted(list(map(int, input('\nВведіть числа через пробіл:\n>>> ').split())))
elif rand_or_inp_BINARY == 2:  
    _BINARY_massive = sorted([random.randint(-10, 10) for i in range(int(input('\nВведіть кількість чисел:\n>>> ')))])

search_BINARY_inp = int(input('\nВведіть:\n'
                              '1 - якщо хочете самостійно ввести число, яке потрібно знайти\n'
                              '2 - якщо хочете згенерувати будь-яке число в діапазоні [-10; 10]\n>>> '))
if search_BINARY_inp == 1: 
    searchBinary = int(input('\nВведіть число:\n>>> '))
elif search_BINARY_inp == 2:  
    searchBinary = random.randint(-10, 10)

#  DIRECT SUBSTRING SEARCH

print('\n<<<<<<<<<<  ПРЯМИЙ ПОШУК ПІДРЯДКА  >>>>>>>>>>\n')
rand_or_inp_DIRECT = int(input('\nВведіть:\n'
                               '1 - якщо хочете ввести дані самостійно\n'
                               '2 - якщо хочете обрати вже підготовлений текст\n>>> '))
if rand_or_inp_DIRECT == 1:  
    _DIRECT_string = input('\nВведіть текст:\n>>> ')
    searchDirect = input('Введіть підрядок: ')
elif rand_or_inp_DIRECT == 2:  
    _DIRECT_string = 'eggsspag spar egspasspameggs esagsspa'
    searchDirect = 'spameggs'

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

linear = linearSearch(_LINEAR_massive, searchLinear)  
binary = binarySearch(_BINARY_massive, searchBinary)  
direct = directSearch(_DIRECT_string, searchDirect)  

print(f'\nЛІНІЙНИЙ ПОШУК\n'
      f'Ваш масив даних: {_LINEAR_massive}')  
print(f'Ваше шукане число {searchLinear} знаходиться на позиції {linear[0]}\n'
      f'Кількість порівнянь: {linear[1]}')
timeLinear = timeit.timeit("linearSearch(_LINEAR_massive, searchLinear)", 
                           setup="from __main__ import linearSearch, _LINEAR_massive, searchLinear", number=1)
print(f'Час, що витратився: {timeLinear:.4e} с.')

print(f'\nБІНАРНИЙ ПОШУК\n'
      f'Ваш масив даних: {_BINARY_massive}')  
print(f'Ваше шукане число {searchBinary} знаходиться на позиції {binary[0]}\n'
      f'Кількість порівнянь: {binary[1]}')
timeBinary = timeit.timeit("binarySearch(_BINARY_massive, searchBinary)", 
                           setup="from __main__ import binarySearch, _BINARY_massive, searchBinary", number=1)
print(f'Час, що витратився: {timeBinary:.4e} с.')

print(f'\nПРЯМИЙ ПОШУК ПІДРЯДКА\n'
      f'Ваш текст: {_DIRECT_string}') 
print(f'Ваше шукане слово {searchDirect} знаходиться в зрізі '
      f'[{direct[0]}:{direct[0] + len(searchDirect) - 1}]\n'
      f'Кількість порівнянь: {direct[1]}')
timeBinary = timeit.timeit("directSearch(_DIRECT_string, searchDirect)",  
                           setup="from __main__ import directSearch, _DIRECT_string, searchDirect", number=1)
print(f'Час, що витратився: {timeBinary:.4e} с.')
