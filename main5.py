import random

my_list = [random.randint(1, 100) for _ in range(20)]
print("Исходный список (20 элементов):", my_list)

n = int(input("Введите число: "))

new_list = [x for x in my_list if x <= n]
print("Новый список:", new_list)