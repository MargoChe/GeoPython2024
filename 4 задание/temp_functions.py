# Функция преобразования температуры из градусов Фаренгейта в градусы Цельсия
def fahr_to_celsius(temp_fahrenheit):
    """
    Преобразует температуру из градусов Фаренгейта в градусы Цельсия.
    """
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    return temp_celsius

# Функция классификации температур
def temp_classifier(temp_celsius):
    """
    Классифицирует температуры по критериям.
    """
    if temp_celsius < -2:
        return 0
    elif -2 <= temp_celsius < 2:
        return 1
    elif 2 <= temp_celsius < 15:
        return 2
    elif temp_celsius >= 15:
        return 3

# DocString для всего скрипта
"""
Скрипт temp_functions.py содержит функции для преобразования температур и классификации их по критериям.
"""
