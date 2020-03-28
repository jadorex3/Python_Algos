"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 45
Введите второе число: 56
Результат 45 + 56 = 101
Введите операцию (+, -, *, / или 0 для выхода): rth
Неверная операция. Повторите ввод
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    OPER_TYPE = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if OPER_TYPE == '0':
        break
    if OPER_TYPE in '+-*/':
        try:
            NUM_1 = float(input('Введите первое число: '))
            NUM_2 = float(input('Введите второе число: '))

            if OPER_TYPE == '+':
                RES = NUM_1 + NUM_2
            elif OPER_TYPE == '-':
                RES = NUM_1 - NUM_2
            elif OPER_TYPE == '*':
                RES = NUM_1 * NUM_2
            elif OPER_TYPE == '/':
                if NUM_2 == 0:
                    RES = NUM_1 / NUM_2
                else:
                    print('Невозможно деление на ноль')
                    continue

            print(f'Результат {NUM_1} {OPER_TYPE} {NUM_2} = {RES}')
        except ValueError:
            print("Введенное значение не является числом")
    else:
        print('Неверная операция. Повторите ввод')
