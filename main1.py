my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print("Исходный список:", my_list)

duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Элементы, встречающиеся более одного раза:", duplicates)