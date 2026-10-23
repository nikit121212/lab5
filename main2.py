list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
print("Первый список:", list1)
print("Второй список:", list2)

list3 = [x for x in list2 if x not in list1]
print("Третий список:", list3)