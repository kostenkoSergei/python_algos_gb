"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform

n = int(input('Введите число элементов: '))
lst = [uniform(0, 50) for _ in range(n)]
print(f'Исходный - {lst}')


def merge(left_lst, right_lst):
    """Выполняет слияние подсписков"""
    sorted_lst = []
    left_lst_index = right_lst_index = 0

    left_lst_length, right_lst_length = len(left_lst), len(right_lst)

    for _ in range(left_lst_length + right_lst_length):
        if left_lst_index < left_lst_length and right_lst_index < right_lst_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его в отсортированный массив
            if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его в отсортированный массив
            else:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1

        # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
        elif left_lst_index == left_lst_length:
            sorted_lst.append(right_lst[right_lst_index])
            right_lst_index += 1
        # Если достигнут конец правого списка, элементы левого списка добавляем в отсортированный массив
        elif right_lst_index == right_lst_length:
            sorted_lst.append(left_lst[left_lst_index])
            left_lst_index += 1

    return sorted_lst


def merge_sort(nums):
    if len(nums) <= 1:  # Базовый случай
        return nums

    mid = len(nums) // 2  # Ищем середину списка

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


print(f'Отсортированный - {merge_sort(lst)}')
