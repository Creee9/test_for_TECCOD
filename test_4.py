"""Написать программу, которая сортирует список строк по длине,
сначала по возрастанию, а затем по убыванию."""


def sorting_strings(strings: list[str]) -> tuple[list[str]]:

    sorted_strings = (
        sorted(strings, key=len), sorted(strings, key=len, reverse=True)
        )

    return sorted_strings


print(sorting_strings(["а", "ааа", "вd", "sdfsdf"]))
