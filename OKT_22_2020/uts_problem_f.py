"""
DESKRIPSI SOAL

Buatlah program untuk menghitung berapa banyak bit nol pada bilangan biner 5
bit. Misalnya diketahui bilangan biner S = “01110” maka outputnya adalah 2.
Input bilangan biner tersebut bertipe string.

PETUNJUK MASUKAN

Input terdiri atas 1 string

PETUNJUK KELUARAN

Outputkan banyak angka 0 yang ada
"""

binary_str = input()

zeroes_count = 0

# Hitung dari belakang
for i in range(1, 5+1):
    if binary_str[-i] == '0':
        zeroes_count += 1

print(zeroes_count)
