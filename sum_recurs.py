def sum_recursive(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum_recursive(a + 1, b - 1)
    else:
        return sum_recursive(a - 1, b + 1)

# Пример использования
result = sum_recursive(2, 2)
print("Sum:", result)  # Вывод результата
