pages_num = int(input())

days_list = ['Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu']

day_index = 0

while pages_num > 0:
    day = days_list[day_index]

    if day == "Jum'at":
        pages_num -= 2
    elif day == 'Minggu':
        pages_num -= 3
    else:
        pages_num -= 1

    if day_index == 6:
        day_index = 0
    else:
        day_index += 1

print(day)
