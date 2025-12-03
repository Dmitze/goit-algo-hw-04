def merge_k_lists(lists):
    # Об'єднуємо кілька відсортованих списків
    if not lists:
        return []
    
    # Функція для злиття двох списків
    def merge_two(list1, list2):
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    # Послідовно об'єднуємо всі списки
    result = lists[0]
    for lst in lists[1:]:
        result = merge_two(result, lst)
    
    return result

# Приклад використання
def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    
    print("Вхідні списки:")
    for i, lst in enumerate(lists):
        print(f"  Список {i+1}: {lst}")
    
    # Об'єднуємо списки
    merged = merge_k_lists(lists)
    
    print(f"\nОб'єднаний відсортований список: {merged}")
    
    # Тестуємо на додаткових даних
    print("\nДодатковий тест:")
    more_lists = [[10, 20, 30], [15, 25], [5, 35, 40]]
    print(f"Списки: {more_lists}")
    print(f"Результат: {merge_k_lists(more_lists)}")

if __name__ == "__main__":
    main()