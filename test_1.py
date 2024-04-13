"""Написать функцию, которая принимает на вход список
целых чисел и возвращает новый список,содержащий только
уникальные элементы из исходного списка."""

duplicate_nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]


def unique_lst(numbers: list) -> list[int]:  # через список
    unique = []
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_lst(duplicate_nums))


def unique_lst(numbers: list) -> list[int]:  # или через множество
    unique_nums = list(set(numbers))
    return unique_nums


print(unique_lst(duplicate_nums))
