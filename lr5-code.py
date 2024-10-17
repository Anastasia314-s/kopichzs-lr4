def is_alternating(arr):
    """
    Проверяет, является ли массив знакочередующимся.
    
    :param arr: Список вещественных чисел
    :return: True если массив знакочередующийся, иначе False
    """
    if len(arr) < 2:
        return True  # Массив из одного элемента или пустой считается знакочередующимся
    
    for i in range(1, len(arr)):
        if arr[i] == 0 or arr[i-1] == 0:
            return False  # Ноль не может быть частью знакочередующейся последовательности
        if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
            return False  # Проверка на одинаковые знаки
    
    return True

# Пример массивов
arrays = [
    [1.5, -2.3, 3.4, -4.5],
    [1.0, -1.0, 2.0, -2.0],
    [3.0, -4.0, 5.0],
    [2.0, 3.0, -1.0],
    [-1.0, 2.0, -3.0]
]

# Проверка массивов
found = False
for index, array in enumerate(arrays):
    if is_alternating(array):
        print(f"Массив номер {index + 1} является знакочередующимся.")
        found = True

if not found:
    print("Нет знакочередующихся массивов.")