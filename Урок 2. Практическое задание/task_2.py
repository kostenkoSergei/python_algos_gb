"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
user_number = int(input('Введите любое натуральное число: '))
i = 0  # счетчик четных цифр
j = 0  # счетчик нечетных цифр


def calc_even(number):
    global i
    global j
    if number // 10 == 0:
        if number % 2 == 0:
            i += 1
        else:
            j += 1
    else:
        if (number % 10) % 2 == 0:
            i += 1
        else:
            j += 1
        calc_even(number // 10)


calc_even(user_number)
print(f'Количество четных и нечетных цифр в числе равно: {i, j}')
