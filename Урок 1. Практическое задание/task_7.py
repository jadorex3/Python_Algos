"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


try:
    PARAM_A = int(input('Введите длину отрезка a = '))
    PARAM_B = int(input('Введите длину отрезка b = '))
    PARAM_C = int(input('Введите длину отрезка c = '))

    if PARAM_A + PARAM_B <= PARAM_C or PARAM_A + \
            PARAM_C <= PARAM_B or PARAM_B + PARAM_C <= PARAM_A:
        print("Треугольник не существует")
    elif PARAM_A != PARAM_B and PARAM_A != PARAM_C and PARAM_B != PARAM_C:
        print("Треугольник разносторонний")
    elif PARAM_A == PARAM_B == PARAM_C:
        print("Треугольник равносторонний")
    else:
        print("Треугольник равнобедренный")

except ValueError:
    print("Введенное значение не является целым числом")
