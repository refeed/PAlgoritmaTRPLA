'''

DESKRIPSI SOAL

Akan dibuat sebuah pengundian doorprize berdasar nama peserta. Pada awalnya,
akan dilist semua nama peserta, kemudian akan dipilih nama peserta yang memiliki
huruf A terbanyak.

PETUNJUK MASUKAN

Input terdiri atas 1 baris nama yang dipisahkan dengan spasi

PETUNJUK KELUARAN

Output terdiri dari 1 nama yang mendapatkan doorprize.

CONTOH MASUKAN

agus budi romi sri restu

CONTOH KELUARAN

agus

'''
name_list = input().split()

def count_a(word):
    sum_a = 0
    for char in word:
        if char == 'a' or char =='A':
            sum_a += 1
    return sum_a

max_a_name = name_list[0]
max_a_name_a_count = count_a(max_a_name)

for name in name_list[1:]:
    name_a_count = count_a(name)
    if name_a_count > max_a_name_a_count:
        max_a_name = name
        max_a_name_a_count = name_a_count

print(max_a_name)
