masukan_str = input()

masukan_int_list = list(map(int, masukan_str.split()))  # Konversi elemen list ke integer

a = masukan_int_list[0]
b = masukan_int_list[1]
c = masukan_int_list[2]

hasil = (a % 3) + (b % 4) + (c % 5)

print(hasil)
