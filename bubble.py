# ==========================================
# 1. БЛОК ФУНКЦИЙ СОРТИРОВКИ
# ==========================================

def bubble_sort(arr):
    """Сортировка пузырьком."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    """Сортировка выбором."""
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    """Сортировка вставками."""
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i
        while j >= 1 and arr[j - 1] > elem:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = elem


# ==========================================
# 2. ЕДИНАЯ ТОЧКА ВХОДА ДЛЯ ТЕСТОВ
# ==========================================
if __name__ == "__main__":
    print("--- Тест сортировки пузырьком ---")
    data_bubble = [64, 34, 25, 12, 22, 11, 90]
    print("До:   ", data_bubble)
    bubble_sort(data_bubble)
    print("После:", data_bubble)
    print()

    print("--- Тест сортировки выбором ---")
    data_selection = [64, 25, 12, 22, 11]
    print("До:   ", data_selection)
    selection_sort(data_selection)
    print("После:", data_selection)
    print()

    print("--- Тест сортировки вставками ---")
    data_insertion = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
    print("До:   ", data_insertion)
    insertion_sort(data_insertion)
    print("После:", data_insertion)
