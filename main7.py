school = {
    "1а": 25,
    "1б": 22,
    "2а": 28,
    "2б": 24,
    "3а": 26,
    "3б": 23,
    "4а": 27,
    "4б": 21,
    "5а": 30,
    "5б": 29,
    "6а": 26,
    "6б": 25,
    "7а": 28,
    "7б": 24,
}

print("school:")
for cls, count in school.items():
    print(f" {cls}: {count} ")

school["5а"] = 32
print(f"\na) {school['5а']} ")

school["8а"] = 27
print(f"b) {school['8а']} ")

del school["4б"]
print("c) Класс 4б удалён")


total = sum(school.values())
print(f"\nОбщее количество учащихся в школе: {total}")

print("\nИтоговый словарь:")
for cls, count in school.items():
    print(f"  Класс {cls}: {count} учеников")