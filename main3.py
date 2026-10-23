my_list = [10, 20, 30, 20, 40, 50]
print("Исходный список:", my_list)

for i in range(len(my_list)):
    if my_list[i] == 20:
        my_list[i] = 200

print("Изменённый список:", my_list)