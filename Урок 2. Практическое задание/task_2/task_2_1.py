"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def cycle_method(num):
    """Цикл"""
    evens = 0
    odds = 0

    while num != 0:
        current_num = num % 10
        num = num // 10
        if current_num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds


try:
    NUM = int(input('Введите натуральное число: '))
    if NUM <= 0:
        raise ValueError

    print(f'В числе {NUM} всего {cycle_method(NUM)[0] + cycle_method(NUM)[1]} цифр, '
          f'из которых {cycle_method(NUM)[0]} чётных и {cycle_method(NUM)[1]} нечётных')

except ValueError:
    print("Введенное значение не является натуральным числом")
