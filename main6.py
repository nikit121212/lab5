my_list = [12, 5, 34, 7, 89, 23, 3, 56]
print("Список:", my_list)

max_val = max(my_list)
min_val = min(my_list)
max_index = my_list.index(max_val)
min_index = my_list.index(min_val)

print(f"Наибольший элемент: {max_val}, индекс: {max_index}")
print(f"Наименьший элемент: {min_val}, индекс: {min_index}")