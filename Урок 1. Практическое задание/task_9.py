"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


import sys

try:
    NUM_1 = int(input('Введите число a = '))
    NUM_2 = int(input('Введите число b = '))
    NUM_3 = int(input('Введите число c = '))

    if NUM_1 == NUM_2 or NUM_1 == NUM_3 or NUM_2 == NUM_3:
        print('Введены равные числа')
        sys.exit(1)
    elif NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
        print(f'Среднее число: {NUM_1}')
    elif NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
        print(f'Среднее число: {NUM_2}')
    else:
        print(f'Среднее число: {NUM_3}')

except ValueError:
    print("Введенное значение не является целым числом")
