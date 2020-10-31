'''
Menghitung volume kerucut
'''
PI = 3.14

masukan_str = input()  # Ekspektasi masukan berupa dua angka dipisah dengan spasi

alas, tinggi = list(map(float, masukan_str.split()))

hasil = ((1/3) * PI * alas**2 * tinggi)

print(hasil)
