my_list = [2, 4, 6, 15, 8, 10]
print("Список:", my_list)

for x in my_list:
    if x == 15:
        print("Встречено число 15. Остановка.")
        break
    if x % 2 == 0:
        print(x)