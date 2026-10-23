import random

my_list = [random.randint(1, 10) for _ in range(10)]
print("Исходный список:", my_list)

my_list = [x ** 2 for x in my_list]
print("Список квадратов:", my_list)