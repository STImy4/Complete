from decimal import Decimal
import re


#Сортирует список чисел с использованием сортировки пузырьком.
def bubble_sort(numbers):
    n = len(numbers)
    
    for i in range(n):
        # Проходим по всем элементам списка
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


#Форматирует число, убирая десятичную часть, если оно целое.
def format_number(number):
    decimal_number = Decimal(number)
    
    if decimal_number == decimal_number.to_integral_value():
        return str(decimal_number.to_integral_value())
    else:
        return str(decimal_number)


def is_valid_number(num_str):
    # Регулярное выражение для проверки чисел
    pattern = r'^-?\d+(\.\d+)?$'
    
    return re.match(pattern, num_str) is not None


#Запрашивает у пользователя ввод чисел и возвращает список валидных чисел.
def get_numbers_from_user():
    while True:
        user_input = input("Введите список чисел, разделённых пробелами: ")
        
        numbers_str = user_input.split()
        
        numbers = []
        
        valid_input = True  # Флаг для отслеживания валидности ввода
        
        for num_str in numbers_str:
            if is_valid_number(num_str):
                numbers.append(Decimal(num_str))  # Используем Decimal для точности
            else:
                print(f"'{num_str}' не является допустимым числом. Пожалуйста, введите только числа.")
                
                valid_input = False  # Устанавливаем флаг в False, если есть ошибка
                
                break  # Выходим из цикла, чтобы запросить ввод заново
        
        if valid_input:
            return numbers  # Если ввод валиден, возвращаем список чисел
        else:
            input("Нажмите на любую кнопку, чтобы повторить ввод.")


def main():
    numbers = get_numbers_from_user()
    
    # Фильтруем четные числа
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    
    # Находим минимальное и максимальное числа
    min_number = min(numbers) if numbers else None
    
    max_number = max(numbers) if numbers else None
    
    
    # Сортируем список по возрастанию
    sorted_numbers = bubble_sort(numbers)
    

    # Форматируем результаты
    formatted_even_numbers = [format_number(num) for num in even_numbers]
    
    formatted_min_number = format_number(min_number) if min_number is not None else "Нет чисел"
    
    formatted_max_number = format_number(max_number) if max_number is not None else "Нет чисел"
    
    formatted_sorted_numbers = [format_number(num) for num in sorted_numbers]
    

    # Выводим результаты
    print("Четные числа:", ", ".join(formatted_even_numbers) if formatted_even_numbers else "Нет четных чисел")
    
    print("Минимальное число:", formatted_min_number)
    
    print("Максимальное число:", formatted_max_number)
    
    print("Отсортированный список:", ", ".join(formatted_sorted_numbers))
    

if __name__ == "__main__":
    main()
    
    input("Нажми на любую кнопку чтоб завершить программу.")
