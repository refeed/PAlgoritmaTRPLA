# Masukan tinggi dan alas, menghitung luas
masukan_str = input()

masukan_float_list = list(map(float, masukan_str.split()))  # Konversi tipe elemen list ke float

alas = masukan_float_list[0]
tinggi = masukan_float_list[1]

hasil = (0.5 * alas * tinggi)

print(hasil)