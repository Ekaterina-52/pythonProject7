import random
numbers = [random.randint(1, 10) for _ in range(10)]
min_number = min(numbers)
average = sum(numbers) / len(numbers)
random_numbers = random.sample(numbers, 2)
random_product = random_numbers[0] * random_numbers[1]
print("Список чисел:", numbers)
print("Наименьшее число:", min_number)
print("Среднее арифметическое:", average)
print("Умножение двух случайных чисел из списка:", random_numbers[0], "*", random_numbers[1], "=", random_product)