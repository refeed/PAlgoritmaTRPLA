"""
DESKRIPSI SOAL

Buatlah program yang menerima 3 buah input nilai dan outputkan jumlah maksimal
dari 2 bilangannya ! diantara ketiga input tersebut.

PETUNJUK MASUKAN

Input terdiri atas 3 angka dalam 1 baris

PETUNJUK KELUARAN

Outputkan angka jumlah terbesar dari 2 angka

"""

a, b, c = list(map(int, input().split()))

sum_values = 0

if a >= b:
    if b >= c:  # a > b > c
        sum_values = a + b
    else:  # a, c, b
        sum_values = a + c
else:  # b > a
    if a >= c:  # b > a > c
        sum_values = a + b
    else:  # b > c > a
        sum_values = b + c

print(sum_values)
