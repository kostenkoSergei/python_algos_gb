"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

users = {'person1': [123, True], 'person2': [145, True], 'person3': [183, False], 'person4': [445, False]}
""" 
Варианты 1 и 2 имеют одинаковую сложность, но первый вариант более предпочтителен из-за лаконичности и использования in
вместо for для итерации по словарю.
"""


# Решение 1. Сложность: O(n). Определяется проходом по словарю
def valid_check1(login, password):
    if login in users.keys() and users[login][0] == password and users[login][1]:  # O(n) + O(1)
        print(f'Добро пожаловать, {login}')
    elif login not in users.keys():  # O(n)
        print('Пользователя с таким логином не существует')
    elif login in users.keys() and users[login][0] == password and not users[login][1]:  # O(n) + O(1)
        print('Ваша учетная запись не активирована')
        user_answer = int(input('Для активации нажмите 1, для выхода 2: '))  # O(1)
        if user_answer == 1:
            users[login][1] = True  # O(1)
            print(f'Добро пожаловать, {login}')
        else:
            print('Сеанс завершен')
    elif login in users.keys() and users[login][0] != password:  # O(n) + O(1)
        print('Вы ввели неправильный пароль')


def main1():
    try:
        login = input('Введите Ваш логин: ')  # O(1)
        password = int(input('Введите Ваш пароль: '))  # O(1)
        valid_check1(login, password)
    except ValueError as err:
        print('Пароль должен быть числовым', err)


# main1()

# Решение 2. Сложность: O(n). Определяется проходом по словарю
def valid_check2(login, password):
    count = 0  # O(1)
    for key, value in users.items():  # O(n)
        if login != key:
            count += 1  # O(1)
            if count == len(users):  # O(1) - len словаря
                print('Пользователя с таким логином не существует')
        elif login == key and value[0] == password and value[1]:
            print(f'Добро пожаловать, {login}')
            break
        elif login == key and value[0] == password and not value[1]:  # O(1)
            print('Ваша учетная запись не активирована')
            user_answer = int(input('Для активации нажмите 1, для выхода 2: '))  # O(1)
            if user_answer == 1:  # O(1)
                users[login][1] = True  # O(1)
                print(f'Добро пожаловать, {login}')
                break
            else:
                print('Сеанс завершен')
                break
        elif login == key and value[0] != password:  # O(1)
            print('Вы ввели неправильный пароль')


def main2():
    try:
        login = input('Введите Ваш логин: ')  # O(1)
        password = int(input('Введите Ваш пароль: '))  # O(1)
        valid_check2(login, password)
    except ValueError as err:
        print('Пароль должен быть числовым', err)


main2()
