import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм сортування злиттям  
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Допоміжна функція для злиття
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Тестування швидкості алгоритмів
def compare_sorting():
    sizes = [100, 1000, 3000]
    
    print("Порівняння алгоритмів сортування")
    print("=" * 60)
    print(f"{'Розмір':<8} {'Insertion Sort':<15} {'Merge Sort':<12} {'Timsort (sorted)':<15}")
    print("-" * 60)
    
    for size in sizes:
        # Створюємо випадковий масив
        data = [random.randint(0, 10000) for _ in range(size)]
        
        time_insertion = timeit.timeit(
            lambda: insertion_sort(data.copy()),
            number=1
        )
        
        time_merge = timeit.timeit(
            lambda: merge_sort(data.copy()),
            number=1
        )
        
        time_timsort = timeit.timeit(
            lambda: sorted(data.copy()),
            number=1
        )
        
        print(f"{size:<8} {time_insertion:<15.5f} {time_merge:<12.5f} {time_timsort:<15.5f}")
    
 