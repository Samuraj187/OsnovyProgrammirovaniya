def count_matching_numbers():
    # Считываем три целых числа через input()
    a, b, c = map(int, input().split())

    # Логика проверки совпадений
    if a == b == c:  # Если все три числа совпадают
        print(3)
    elif a == b or a == c or b == c:  # Если совпадают только два числа
        print(2)
    else:  # Если все числа различны
        print(0)

# Вызов функции
count_matching_numbers()
