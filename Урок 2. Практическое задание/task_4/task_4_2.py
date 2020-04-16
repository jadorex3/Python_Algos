"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recur_method(count, summ=1, num=1):
    """Рекурсия"""
    if not count - 1:
        return summ
    else:
        num = num / (-2)
        summ += num
        count -= 1
        return recur_method(count, summ, num)


try:
    NUM = int(input('Введите количество элементов: '))
    if NUM <= 0:
        raise ValueError
    print(f'Количество элементов - {NUM}, их сумма - {recur_method(NUM)}')
except ValueError:
    print("Введенное значение не является натуральным числом")
