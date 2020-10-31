# abc hasilnya a*b + c

masukan_str = input()

masukan_int_list = list(map(int, masukan_str.split()))

a = masukan_int_list[0]
b = masukan_int_list[1]
c = masukan_int_list[2]

hasil = a * b + c

print(hasil)
