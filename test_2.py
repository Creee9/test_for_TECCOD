"""Написать функцию, которая принимает на вход
два целых числа (минимум и максимум) и возвращает
список всех простых чисел в заданном диапазоне."""


def is_prime(num: int) -> bool:
    """Функция для квалификации числа как простого."""
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def prime_nums(a: int, b: int) -> list[int]:
    return [i for i in range(a, b + 1) if is_prime(i)]


print(prime_nums(-100, 100))
