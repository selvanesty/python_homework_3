import numpy as np

# 1. Одновимірний масив з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, 200)
print("Початковий масив (перші 20 елементів):")
print(array[:20])

# 2. Використовуючи маску, відфільтруйте всі додатні числа
mask_positive = array > 0
positive_numbers = array[mask_positive]
print("\nДодатні числа (перші 20):")
print(positive_numbers[:20])

# 3. Замініть всі від’ємні значення на нулі
processed_array = array.copy()
processed_array[processed_array < 0] = 0
print("\nМасив після заміни від'ємних чисел на 0 (перші 20):")
print(processed_array[:20])

# 4. Обчисліть середнє значення отриманого масиву
average_value = np.mean(processed_array)
print(f"\nСереднє значення отриманого масиву: {average_value:.2f}")